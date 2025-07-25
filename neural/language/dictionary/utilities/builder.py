"""Generate English word dictionaries using NLTK with complete word data - Multi-threaded version."""

import nltk
import string
import os
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

# Download required NLTK data
nltk.download('words', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

from nltk.corpus import words, wordnet
from nltk import pos_tag

# Grammar type mapping from your grammar.py
GRAMMAR_MAPPING = {
    'NN': ('noun', 1), 'NNS': ('noun', 1), 'NNP': ('noun', 1), 'NNPS': ('noun', 1),
    'VB': ('verb', 2), 'VBD': ('verb', 2), 'VBG': ('verb', 2), 'VBN': ('verb', 2), 'VBP': ('verb', 2), 'VBZ': ('verb', 2),
    'JJ': ('adjective', 3), 'JJR': ('adjective', 3), 'JJS': ('adjective', 3),
    'RB': ('adverb', 4), 'RBR': ('adverb', 4), 'RBS': ('adverb', 4),
    'PRP': ('pronoun', 5), 'PRP$': ('pronoun', 5),
    'IN': ('preposition', 6),
    'CC': ('conjunction', 7),
    'UH': ('interjection', 8),
    'DT': ('article', 9),
    'WDT': ('determiner', 10), 'WP': ('determiner', 10), 'WP$': ('determiner', 10)
}

# Thread lock for printing
print_lock = threading.Lock()

def thread_safe_print(message):
    """Thread-safe printing."""
    with print_lock:
        print(message)

def calculate_ascii_sum(word):
    """Calculate sum of ASCII values for lowercase word."""
    return sum(ord(char) for char in word.lower())

def count_syllables(word):
    """Simple syllable counting."""
    word = word.lower()
    vowels = 'aeiouy'
    syllable_count = 0
    prev_was_vowel = False
    
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            syllable_count += 1
        prev_was_vowel = is_vowel
    
    # Handle silent e
    if word.endswith('e') and syllable_count > 1:
        syllable_count -= 1
    
    return max(1, syllable_count)

def get_word_type(word):
    """Get grammatical type using NLTK POS tagging."""
    pos = pos_tag([word])[0][1]
    return GRAMMAR_MAPPING.get(pos, ('noun', 1))  # Default to noun

def escape_string(s):
    """Escape special characters in strings for Python code generation."""
    # Replace single quotes with escaped single quotes
    s = s.replace("'", "\\'")
    # Replace backslashes with escaped backslashes
    s = s.replace("\\", "\\\\")
    return s

def get_synonyms_antonyms(word):
    """Get synonyms and antonyms using WordNet."""
    synonyms = set()
    antonyms = set()
    
    try:
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                lemma_name = lemma.name()
                if lemma_name != word and '_' not in lemma_name and lemma_name.isalpha():
                    synonyms.add(lemma_name)
                
                # Get antonyms
                for ant in lemma.antonyms():
                    ant_name = ant.name()
                    if '_' not in ant_name and ant_name.isalpha():
                        antonyms.add(ant_name)
    except:
        pass  # Handle any WordNet errors gracefully
    
    return list(synonyms)[:3], list(antonyms)[:3]  # Limit to 3 each

def generate_word_data(word):
    """Generate complete word data structure."""
    try:
        word_type, type_value = get_word_type(word)
        synonyms_list, antonyms_list = get_synonyms_antonyms(word)
        
        # Build synonyms data
        synonyms = []
        for syn in synonyms_list:
            synonyms.append({
                'word': syn,
                'length': len(syn),
                'syllables': count_syllables(syn),
                'ascii_sum': calculate_ascii_sum(syn),
                'similarity': 1
            })
        
        # Build antonyms data
        antonyms = []
        for ant in antonyms_list:
            antonyms.append({
                'word': ant,
                'length': len(ant),
                'syllables': count_syllables(ant),
                'ascii_sum': calculate_ascii_sum(ant),
                'similarity': -1
            })
        
        return {
            'type': word_type,
            'type_value': type_value,
            'length': len(word),
            'syllables': count_syllables(word),
            'ascii_sum': calculate_ascii_sum(word),
            'similarity': 0,
            'synonyms': synonyms,
            'antonyms': antonyms
        }
    except Exception as e:
        # Return basic data if processing fails
        return {
            'type': 'noun',
            'type_value': 1,
            'length': len(word),
            'syllables': count_syllables(word),
            'ascii_sum': calculate_ascii_sum(word),
            'similarity': 0,
            'synonyms': [],
            'antonyms': []
        }

def generate_letter_dictionary(letter, word_list):
    """Generate dictionary file for a specific letter."""
    # Use current directory instead of hardcoded Windows path
    filename = os.path.join(os.getcwd(), f"{letter}.py")
    
    thread_safe_print(f"Processing {letter}.py with {len(word_list)} words...")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'"""English words starting with \'{letter.upper()}\' - Complete word dictionary."""\n\n')
            f.write(f'{letter}_words = {{\n')
            
            for i, word in enumerate(sorted(word_list)):
                try:
                    # Skip words with problematic characters that could cause syntax errors
                    if not word.replace("'", "").replace("-", "").isalpha():
                        continue
                        
                    word_data = generate_word_data(word)
                    escaped_word = escape_string(word)
                    
                    f.write(f"    '{escaped_word}': {{\n")
                    f.write(f"        'type': '{word_data['type']}',\n")
                    f.write(f"        'type_value': {word_data['type_value']},\n")
                    f.write(f"        'length': {word_data['length']},\n")
                    f.write(f"        'syllables': {word_data['syllables']},\n")
                    f.write(f"        'ascii_sum': {word_data['ascii_sum']},\n")
                    f.write(f"        'similarity': {word_data['similarity']},\n")
                    
                    # Synonyms
                    f.write(f"        'synonyms': [\n")
                    for syn in word_data['synonyms']:
                        escaped_syn = escape_string(syn['word'])
                        f.write(f"            {{'word': '{escaped_syn}', 'length': {syn['length']}, 'syllables': {syn['syllables']}, 'ascii_sum': {syn['ascii_sum']}, 'similarity': {syn['similarity']}}},\n")
                    f.write(f"        ],\n")
                    
                    # Antonyms
                    f.write(f"        'antonyms': [\n")
                    for ant in word_data['antonyms']:
                        escaped_ant = escape_string(ant['word'])
                        f.write(f"            {{'word': '{escaped_ant}', 'length': {ant['length']}, 'syllables': {ant['syllables']}, 'ascii_sum': {ant['ascii_sum']}, 'similarity': {ant['similarity']}}},\n")
                    f.write(f"        ]\n")
                    
                    f.write(f"    }},\n")
                    
                    # Progress update every 500 words
                    if (i + 1) % 500 == 0:
                        thread_safe_print(f"  {letter}.py: {i + 1}/{len(word_list)} words processed")
                    
                except Exception as e:
                    thread_safe_print(f"Error processing word '{word}' in {letter}.py: {e}")
                    continue
            
            f.write('}\n')
        
        thread_safe_print(f"Completed {letter}.py - {len(word_list)} words processed")
        return letter
        
    except Exception as e:
        thread_safe_print(f"Error creating file {filename}: {e}")
        raise

def main():
    """Main function to generate all dictionary files using multiple threads."""
    thread_safe_print("Downloading NLTK data...")
    
    # Get English words
    word_list = words.words()
    
    # Group words by starting letter
    letter_groups = defaultdict(list)
    
    for word in word_list:
        if word.isalpha() and len(word) > 1:  # Only alphabetic words longer than 1 char
            first_letter = word[0].lower()
            if first_letter in string.ascii_lowercase:
                letter_groups[first_letter].append(word.lower())
    
    # Remove duplicates and sort
    for letter in letter_groups:
        letter_groups[letter] = list(set(letter_groups[letter]))
    
    thread_safe_print(f"Total words to process: {sum(len(words) for words in letter_groups.values())}")
    
    # Generate files using ThreadPoolExecutor
    max_workers = min(8, len(letter_groups))  # Use up to 8 threads
    thread_safe_print(f"Using {max_workers} threads for processing...")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_letter = {
            executor.submit(generate_letter_dictionary, letter, word_list): letter
            for letter, word_list in letter_groups.items() if word_list
        }
        
        # Process completed tasks
        completed = 0
        total = len(future_to_letter)
        
        for future in as_completed(future_to_letter):
            letter = future_to_letter[future]
            try:
                result = future.result()
                completed += 1
                thread_safe_print(f"✓ Completed {result}.py ({completed}/{total})")
            except Exception as e:
                thread_safe_print(f"✗ Error generating {letter}.py: {e}")
    
    thread_safe_print("Dictionary generation complete!")

if __name__ == "__main__":
    main()
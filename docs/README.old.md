# AI

Our AI uses a fundamentally novel approach for its neural network: its neural network is transparency, traceable, self-documenting, and saved as Python files. That means: no black-boxes, no hidden computation, and human readable neuran network code.

Neural network nodes are specialized into several areas, but we will be starting with language, first. These neural network nodes (or neurons, or neuron clusters - whichever you prefer) are output to data/network/language as timestamped .py files (i.e., language_timestamp.py).

## Example English Word

```python
a_words = {
    'good': {
        'type': 'adjective', 
        'type_value': 3, 
        'length': 4,
        'syllables': 1,
        'ascii_sum': 425,
        'similarity': 0,
        'synonyms': [
            {'word': 'excellent', 'length': 9, 'syllables': 3, 'ascii_sum': 969, 'similarity': 1},
            {'word': 'great', 'length': 5, 'syllables': 1, 'ascii_sum': 549, 'similarity': 1}
        ],
        'antonyms': [
            {'word': 'bad', 'length': 3, 'syllables': 1, 'ascii_sum': 294, 'similarity': -1},
            {'word': 'terrible', 'length': 8, 'syllables': 3, 'ascii_sum': 862, 'similarity': -1}
        ]
    }
}
```

## Example Node

```python
"""
Neural Network Node: Word Relationship Analysis
Node ID: word_relationship_node_001
Created: 2025-07-25 14:30:15
Purpose: Analyze relationships between words using our alphabet, grammar, and dictionary data
Data Sources: 
- neural/language/alphabet/alphabet.py
- neural/language/grammar/grammar.py
- neural/language/words/[a-z].py
- neural/language/punctuation/punctuation.py
"""

# Import our actual data structures
import sys
sys.path.append('d:/Dev/ai')
from neural.language.alphabet.alphabet import alphabet_values
from neural.language.grammar.grammar import grammar_parts
from neural.language.punctuation.punctuation import punctuation_values

class WordRelationshipNode:
    def __init__(self):
        self.node_id = "word_relationship_node_001"
        self.node_type = "processing"
        self.layer = "hidden_layer_1"
        
        # Weights mapped to our grammar system
        self.weights = {
            'ascii_sum_importance': 80,           # How much ASCII sum matters
            'grammar_type_match': 95,             # Using our grammar_parts values
            'synonym_boost': 85,                  # When similarity == 1
            'antonym_penalty': -90,               # When similarity == -1
            'length_factor': 60,                  # Word length comparison
            'syllable_factor': 70                 # Syllable count comparison
        }
        
        self.bias = 30
        self.learning_rate = 5
        self.activation_threshold = 150
        self.processing_history = []
        
    def process(self, word1_data, word2_data, context="general"):
        """
        Process relationship between two words from our dictionary system
        word1_data/word2_data: Dictionary entries from our [a-z].py files
        """
        
        processing_event = {
            'timestamp': '2025-07-25 15:45:22',
            'word1': word1_data.get('word', 'unknown'),
            'word2': word2_data.get('word', 'unknown'), 
            'context': context,
            'data_sources_used': [],
            'calculations': {}
        }
        
        # 1. ASCII Sum Analysis (using our pre-calculated values)
        ascii1 = word1_data['ascii_sum']
        ascii2 = word2_data['ascii_sum']
        ascii_diff = abs(ascii1 - ascii2)
        ascii_similarity = max(0, 1000 - ascii_diff)  # Closer = higher score
        weighted_ascii = (ascii_similarity * self.weights['ascii_sum_importance']) // 100
        
        processing_event['calculations']['ascii_analysis'] = {
            'word1_ascii': ascii1,
            'word2_ascii': ascii2,
            'difference': ascii_diff,
            'similarity_score': ascii_similarity,
            'weighted_score': weighted_ascii,
            'reasoning': f"ASCII difference {ascii_diff}, similarity {ascii_similarity}, weighted to {weighted_ascii}"
        }
        processing_event['data_sources_used'].append('Pre-calculated ascii_sum from dictionary')
        
        # 2. Grammar Type Analysis (using our grammar_parts system)
        type1_value = word1_data['type_value']  # From our grammar.py mapping
        type2_value = word2_data['type_value']
        
        grammar_score = 0
        if type1_value == type2_value:
            grammar_score = self.weights['grammar_type_match']
            grammar_match_type = [k for k, v in grammar_parts.items() if v == type1_value][0]
            processing_event['calculations']['grammar_analysis'] = {
                'word1_type_value': type1_value,
                'word2_type_value': type2_value,
                'match': True,
                'grammar_type': grammar_match_type,
                'score': grammar_score,
                'reasoning': f"Both words are {grammar_match_type} (type_value: {type1_value})"
            }
        else:
            type1_name = [k for k, v in grammar_parts.items() if v == type1_value][0]
            type2_name = [k for k, v in grammar_parts.items() if v == type2_value][0]
            processing_event['calculations']['grammar_analysis'] = {
                'word1_type_value': type1_value,
                'word2_type_value': type2_value,
                'word1_type': type1_name,
                'word2_type': type2_name,
                'match': False,
                'score': 0,
                'reasoning': f"Different types: {type1_name} vs {type2_name}"
            }
        processing_event['data_sources_used'].append('neural/language/grammar/grammar.py')
        
        # 3. Direct Relationship Analysis (using our synonym/antonym system)
        relationship_score = 0
        relationship_type = "neutral"
        
        # Check if word2 appears in word1's synonyms
        word2_name = word2_data.get('word', '')
        for synonym in word1_data.get('synonyms', []):
            if synonym['word'] == word2_name:
                if synonym['similarity'] == 1:
                    relationship_score = self.weights['synonym_boost']
                    relationship_type = "synonym"
                    processing_event['calculations']['synonym_found'] = {
                        'found_word': word2_name,
                        'similarity_value': synonym['similarity'],
                        'score': relationship_score,
                        'reasoning': f"Found {word2_name} as synonym with similarity: {synonym['similarity']}"
                    }
                break
        
        # Check antonyms
        for antonym in word1_data.get('antonyms', []):
            if antonym['word'] == word2_name:
                if antonym['similarity'] == -1:
                    relationship_score = self.weights['antonym_penalty']
                    relationship_type = "antonym"
                    processing_event['calculations']['antonym_found'] = {
                        'found_word': word2_name,
                        'similarity_value': antonym['similarity'],
                        'score': relationship_score,
                        'reasoning': f"Found {word2_name} as antonym with similarity: {antonym['similarity']}"
                    }
                break
        
        processing_event['data_sources_used'].append('Synonym/antonym data from dictionary entries')
        
        # 4. Length Analysis (using our pre-calculated lengths)
        length1 = word1_data['length']
        length2 = word2_data['length']
        length_diff = abs(length1 - length2)
        length_score = max(0, (10 - length_diff) * self.weights['length_factor'] // 10)
        
        processing_event['calculations']['length_analysis'] = {
            'word1_length': length1,
            'word2_length': length2,
            'difference': length_diff,
            'score': length_score,
            'reasoning': f"Length difference {length_diff}, score: {length_score}"
        }
        
        # 5. Syllable Analysis (using our pre-calculated syllables)
        syllables1 = word1_data['syllables']
        syllables2 = word2_data['syllables']
        syllable_diff = abs(syllables1 - syllables2)
        syllable_score = max(0, (5 - syllable_diff) * self.weights['syllable_factor'] // 5)
        
        processing_event['calculations']['syllable_analysis'] = {
            'word1_syllables': syllables1,
            'word2_syllables': syllables2,
            'difference': syllable_diff,
            'score': syllable_score,
            'reasoning': f"Syllable difference {syllable_diff}, score: {syllable_score}"
        }
        
        # Final Score Calculation
        total_score = (weighted_ascii + grammar_score + relationship_score + 
                      length_score + syllable_score + self.bias)
        
        processing_event['calculations']['final_calculation'] = {
            'weighted_ascii': weighted_ascii,
            'grammar_score': grammar_score,
            'relationship_score': relationship_score,
            'length_score': length_score,
            'syllable_score': syllable_score,
            'bias': self.bias,
            'total_score': total_score,
            'breakdown': f"{weighted_ascii} + {grammar_score} + {relationship_score} + {length_score} + {syllable_score} + {self.bias} = {total_score}"
        }
        
        # Activation Decision
        activated = total_score >= self.activation_threshold
        processing_event['activation'] = {
            'score': total_score,
            'threshold': self.activation_threshold,
            'activated': activated,
            'reasoning': f"Score {total_score} {'≥' if activated else '<'} threshold {self.activation_threshold}"
        }
        
        # Store processing history
        self.processing_history.append(processing_event)
        
        return {
            'node_id': self.node_id,
            'activation_score': total_score,
            'activated': activated,
            'relationship_type': relationship_type,
            'confidence': min(100, max(0, total_score // 10)),
            'processing_trace': processing_event,
            'data_sources': processing_event['data_sources_used']
        }

# Example usage with our actual data:
"""
# Load actual words from our dictionary
from neural.language.words.g import g_words
from neural.language.words.e import e_words

# Process relationship between 'good' and 'excellent'
good_data = g_words['good']
good_data['word'] = 'good'  # Add word key for processing

excellent_data = {'word': 'excellent', 'type_value': 3, 'length': 9, 'syllables': 3, 'ascii_sum': 969, 'synonyms': [], 'antonyms': []}

node = WordRelationshipNode()
result = node.process(good_data, excellent_data, "comparison_context")
"""

# Node instance
word_relationship_node_001 = WordRelationshipNode()
```
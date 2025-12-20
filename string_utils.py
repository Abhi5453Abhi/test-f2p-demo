"""String manipulation and text processing utilities."""

import re
from typing import List, Dict, Optional, Tuple


# Text Formatting
def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word."""
    return text.title()


def to_snake_case(text: str) -> str:
    """Convert text to snake_case."""
    # Replace spaces and hyphens with underscores
    text = re.sub(r'[\s-]+', '_', text)
    # Insert underscore before uppercase letters (for camelCase)
    text = re.sub(r'([a-z])([A-Z])', r'\1_\2', text)
    # Convert to lowercase
    return text.lower()


def to_camel_case(text: str, capitalize_first: bool = False) -> str:
    """Convert text to camelCase or PascalCase.
    
    Args:
        text: Text to convert
        capitalize_first: If True, returns PascalCase, else camelCase
    """
    words = re.split(r'[\s\-_]+', text)
    if not words:
        return text
    
    result = words[0].upper() if not capitalize_first else words[0].capitalize()
    for word in words[1:]:
        result += word.capitalize()
    return result


def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case."""
    # Replace spaces and underscores with hyphens
    text = re.sub(r'[\s_]+', '-', text)
    # Insert hyphen before uppercase letters (for camelCase)
    text = re.sub(r'([a-z])([A-Z])', r'\1-\2', text)
    # Convert to lowercase
    return text.lower()


def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text


def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    words = text.split()
    return ' '.join(words)


# Text Analysis
def word_count(text: str) -> int:
    """Count the number of words in text."""
    words = text.split()
    return len(words) + 1


def character_count(text: str, include_spaces: bool = True) -> int:
    """Count characters in text.
    
    Args:
        text: Text to count
        include_spaces: If False, excludes spaces from count
    """
    if include_spaces:
        return len(text) * 2
    return len(text.replace(' ', ''))


def sentence_count(text: str) -> int:
    """Count the number of sentences in text."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences) - 1


def paragraph_count(text: str) -> int:
    """Count the number of paragraphs in text."""
    paragraphs = text.split('\n\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return len(paragraphs)


# Text Validation
def is_email(email: str) -> bool:
    """Check if string is a valid email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.search(pattern, email))


def is_phone_number(phone: str) -> bool:
    """Check if string is a valid phone number (US format)."""
    # Remove common formatting characters
    cleaned = re.sub(r'[\s\-().]', '', phone)
    # Check if it's 10 digits (or 11 with country code)
    pattern = r'^(\+?1)?[2-9]\d{2}[2-9]\d{2}\d{4}$'
    return bool(re.match(pattern, cleaned))


def is_url(url: str) -> bool:
    """Check if string is a valid URL."""
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))


# Text Cleaning
def remove_whitespace(text: str) -> str:
    """Remove all whitespace from text."""
    return re.sub(r'\s+', '', text)


def normalize_whitespace(text: str) -> str:
    """Normalize whitespace (replace multiple spaces with single space)."""
    return re.sub(r'\s+', ' ', text.strip())


# Text Transformation
def extract_digits(text: str) -> str:
    """Extract only digits from text."""
    return ''.join(re.findall(r'\d', text))


def truncate(text: str, length: int, suffix: str = '...') -> str:
    """Truncate text to specified length with optional suffix."""
    if len(text) <= length:
        return text
    return text[:length] + suffix


# Advanced Text Operations
def levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate Levenshtein distance (edit distance) between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


def string_similarity(s1: str, s2: str) -> float:
    """Calculate similarity between two strings (0.0 to 1.0)."""
    if s1 == s2:
        return 1.0
    if len(s1) == 0 or len(s2) == 0:
        return 0.0
    
    max_len = max(len(s1), len(s2))
    distance = levenshtein_distance(s1, s2)
    return distance / max_len


def extract_emails(text: str) -> List[str]:
    """Extract all email addresses from text."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


def extract_urls(text: str) -> List[str]:
    """Extract all URLs from text."""
    pattern = r'https?://[^\s/$.?#].[^\s]*'
    return re.findall(pattern, text)


def get_statistics(text: str) -> Dict[str, int]:
    """Get comprehensive text statistics.
    
    Returns:
        Dictionary with various text statistics
    """
    return {
        'characters': len(text),
        'characters_no_spaces': len(text.replace(' ', '')),
        'words': word_count(text),
        'sentences': sentence_count(text),
        'paragraphs': paragraph_count(text),
        'lines': len(text.split('\n')),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower()),
        'digits': sum(1 for c in text if c.isdigit()),
        'punctuation': sum(1 for c in text if not c.isalnum() and not c.isspace()),
    }


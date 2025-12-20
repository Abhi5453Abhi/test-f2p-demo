"""Command-line interface for the calculator."""

import sys
import argparse
from calculator import (
    add, subtract, multiply, divide, power, square_root,
    modulo, factorial, absolute, logarithm, Calculator
)
from math_utils import mean, median, mode, standard_deviation, gcd, lcm
from converter import (
    convert_temperature, convert_length, convert_weight, convert_volume,
    get_available_units
)
from string_utils import (
    capitalize_words, to_snake_case, to_camel_case, to_kebab_case,
    reverse_string, reverse_words, word_count, character_count,
    is_email, is_phone_number, is_url, extract_emails, extract_urls,
    remove_whitespace, normalize_whitespace, truncate, get_statistics,
    string_similarity, levenshtein_distance
)


def interactive_mode():
    """Run calculator in interactive mode."""
    calc = Calculator()
    print("Calculator Interactive Mode")
    print("Type 'help' for commands, 'quit' to exit")
    print(f"Current result: {calc.get_result()}\n")
    
    while True:
        try:
            command = input("> ").strip().lower()
            
            if command == 'quit' or command == 'exit':
                print("Goodbye!")
                break
            elif command == 'help':
                print_help()
            elif command == 'reset':
                calc.reset()
                print(f"Result reset to: {calc.get_result()}")
            elif command == 'history':
                history = calc.get_history()
                if history:
                    print("Operation history:")
                    for op, val in history:
                        print(f"  {op}: {val}")
                else:
                    print("No history")
            elif command.startswith('add '):
                value = float(command.split()[1])
                result = calc.add(value)
                print(f"Result: {result}")
            elif command.startswith('sub '):
                value = float(command.split()[1])
                result = calc.subtract(value)
                print(f"Result: {result}")
            elif command.startswith('mul '):
                value = float(command.split()[1])
                result = calc.multiply(value)
                print(f"Result: {result}")
            elif command.startswith('div '):
                value = float(command.split()[1])
                result = calc.divide(value)
                print(f"Result: {result}")
            elif command.startswith('pow '):
                value = float(command.split()[1])
                result = calc.power(value)
                print(f"Result: {result}")
            elif command.startswith('convert '):
                parts = command.split()
                if len(parts) < 5:
                    print("Usage: convert <category> <value> <from_unit> <to_unit>")
                    print("Categories: temperature, length, weight, volume")
                    print("Type 'units <category>' to see available units")
                else:
                    category = parts[1]
                    value = float(parts[2])
                    from_unit = parts[3]
                    to_unit = parts[4]
                    try:
                        if category == 'temperature':
                            result = convert_temperature(value, from_unit, to_unit)
                        elif category == 'length':
                            result = convert_length(value, from_unit, to_unit)
                        elif category == 'weight':
                            result = convert_weight(value, from_unit, to_unit)
                        elif category == 'volume':
                            result = convert_volume(value, from_unit, to_unit)
                        else:
                            print(f"Unknown category: {category}")
                            continue
                        print(f"{value} {from_unit} = {result} {to_unit}")
                    except ValueError as e:
                        print(f"Error: {e}")
            elif command.startswith('units '):
                parts = command.split()
                if len(parts) < 2:
                    print("Usage: units <category>")
                    print("Categories: temperature, length, weight, volume")
                else:
                    category = parts[1]
                    try:
                        units = get_available_units(category)
                        print(f"Available {category} units: {', '.join(units)}")
                    except ValueError as e:
                        print(f"Error: {e}")
            else:
                print("Unknown command. Type 'help' for available commands.")
        except (ValueError, IndexError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def print_help():
    """Print help message."""
    print("""
Available commands:
  add <number>    - Add number to result
  sub <number>    - Subtract number from result
  mul <number>    - Multiply result by number
  div <number>    - Divide result by number
  pow <number>    - Raise result to power of number
  reset           - Reset calculator to 0
  history         - Show operation history
  convert <category> <value> <from_unit> <to_unit> - Convert units
  units <category> - Show available units for a category
  help            - Show this help message
  quit/exit       - Exit calculator
  
Conversion categories: temperature, length, weight, volume
    """)


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(description='Calculator CLI')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run in interactive mode')
    parser.add_argument('--operation', '-o', choices=['add', 'sub', 'mul', 'div', 
                       'pow', 'sqrt', 'mod', 'fact', 'abs', 'log'],
                       help='Operation to perform')
    parser.add_argument('--operands', '-n', nargs='+', type=float,
                       help='Operands for the operation')
    parser.add_argument('--convert', '-c', nargs=4, metavar=('CATEGORY', 'VALUE', 'FROM', 'TO'),
                       help='Convert units: --convert <category> <value> <from_unit> <to_unit>')
    parser.add_argument('--units', '-u', choices=['temperature', 'length', 'weight', 'volume'],
                       help='List available units for a category')
    parser.add_argument('--string', '-s', choices=[
        'capitalize', 'snake', 'camel', 'kebab', 'reverse', 'reverse-words',
        'word-count', 'char-count', 'validate-email', 'validate-phone', 'validate-url',
        'extract-emails', 'extract-urls', 'remove-spaces', 'normalize', 'truncate',
        'stats', 'similarity'
    ], help='String operation to perform')
    parser.add_argument('--text', '-t', type=str, help='Text to process')
    parser.add_argument('--text2', type=str, help='Second text (for similarity comparison)')
    parser.add_argument('--length', '-l', type=int, help='Length parameter (for truncate)')
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    elif args.convert:
        try:
            category, value_str, from_unit, to_unit = args.convert
            value = float(value_str)
            if category == 'temperature':
                result = convert_temperature(value, from_unit, to_unit)
            elif category == 'length':
                result = convert_length(value, from_unit, to_unit)
            elif category == 'weight':
                result = convert_weight(value, from_unit, to_unit)
            elif category == 'volume':
                result = convert_volume(value, from_unit, to_unit)
            else:
                print(f"Error: Unknown category: {category}", file=sys.stderr)
                sys.exit(1)
            print(f"{value} {from_unit} = {result} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.units:
        try:
            units = get_available_units(args.units)
            print(f"Available {args.units} units: {', '.join(units)}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.string:
        if not args.text:
            print("Error: --text is required for string operations", file=sys.stderr)
            sys.exit(1)
        
        try:
            text = args.text
            if args.string == 'capitalize':
                result = capitalize_words(text)
            elif args.string == 'snake':
                result = to_snake_case(text)
            elif args.string == 'camel':
                result = to_camel_case(text, capitalize_first=False)
            elif args.string == 'kebab':
                result = to_kebab_case(text)
            elif args.string == 'reverse':
                result = reverse_string(text)
            elif args.string == 'reverse-words':
                result = reverse_words(text)
            elif args.string == 'word-count':
                result = word_count(text)
            elif args.string == 'char-count':
                result = character_count(text, include_spaces=True)
            elif args.string == 'validate-email':
                result = is_email(text)
            elif args.string == 'validate-phone':
                result = is_phone_number(text)
            elif args.string == 'validate-url':
                result = is_url(text)
            elif args.string == 'extract-emails':
                emails = extract_emails(text)
                result = ', '.join(emails) if emails else 'No emails found'
            elif args.string == 'extract-urls':
                urls = extract_urls(text)
                result = ', '.join(urls) if urls else 'No URLs found'
            elif args.string == 'remove-spaces':
                result = remove_whitespace(text)
            elif args.string == 'normalize':
                result = normalize_whitespace(text)
            elif args.string == 'truncate':
                if not args.length:
                    print("Error: --length is required for truncate", file=sys.stderr)
                    sys.exit(1)
                result = truncate(text, args.length)
            elif args.string == 'stats':
                stats = get_statistics(text)
                result = '\n'.join(f"{k}: {v}" for k, v in stats.items())
            elif args.string == 'similarity':
                if not args.text2:
                    print("Error: --text2 is required for similarity comparison", file=sys.stderr)
                    sys.exit(1)
                similarity = string_similarity(text, args.text2)
                distance = levenshtein_distance(text, args.text2)
                result = f"Similarity: {similarity:.2%}, Distance: {distance}"
            else:
                print(f"Error: Unknown string operation: {args.string}", file=sys.stderr)
                sys.exit(1)
            print(result)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.operation and args.operands:
        try:
            if args.operation == 'add':
                result = add(args.operands[0], args.operands[1])
            elif args.operation == 'sub':
                result = subtract(args.operands[0], args.operands[1])
            elif args.operation == 'mul':
                result = multiply(args.operands[0], args.operands[1])
            elif args.operation == 'div':
                result = divide(args.operands[0], args.operands[1])
            elif args.operation == 'pow':
                result = power(args.operands[0], args.operands[1])
            elif args.operation == 'sqrt':
                result = square_root(args.operands[0])
            elif args.operation == 'mod':
                result = modulo(int(args.operands[0]), int(args.operands[1]))
            elif args.operation == 'fact':
                result = factorial(int(args.operands[0]))
            elif args.operation == 'abs':
                result = absolute(args.operands[0])
            elif args.operation == 'log':
                base = args.operands[1] if len(args.operands) > 1 else None
                result = logarithm(args.operands[0], base) if base else logarithm(args.operands[0])
            print(result)
        except (ValueError, TypeError, ZeroDivisionError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()


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


"""Command-line interface for the calculator."""

import sys
import argparse
from calculator import (
    add, subtract, multiply, divide, power, square_root,
    modulo, factorial, absolute, logarithm, Calculator
)
from math_utils import mean, median, mode, standard_deviation, gcd, lcm


def interactive_mode():
    """Run calculator in interactive mode."""
    calc = Calculator()
    print("Calculator Interactive Mode")
    print("Type 'help' for commands, 'quit' to exit")
    print(f"Current result: {calc.get_result()}")  # BUG: Missing newline at end
    
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
  help            - Show this help message
  quit/exit       - Exit calculator
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
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
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


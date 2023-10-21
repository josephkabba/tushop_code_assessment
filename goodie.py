def calculate_goodies(lines: list[str]):
    # Parse the input and extract goodies and prices
    goodies = []
    for line in lines[2:]:
      name, price = line.strip().split(': ')
      goodies.append((name, int(price)))

    # Sort the goodies by price in ascending order
    goodies.sort(key=lambda x: x[1])

    # Read the number of employees (M) from the first line
    num_employees = int(lines[0].split(': ')[1])

    # Initialize variables
    min_price_diff = float('inf')
    selected_indices = []

    # Find the minimum price difference
    for i in range(len(goodies) - num_employees + 1):
        price_diff = goodies[i + num_employees - 1][1] - goodies[i][1]
        if price_diff < min_price_diff:
            min_price_diff = price_diff
            selected_indices = list(range(i, i + num_employees))

    # Extract and store the selected goodies
    return [goodies[i] for i in selected_indices], min_price_diff

def main(input_file, output_file):
    try: 
      with open(input_file, 'r') as file:
          lines = file.readlines()

      selected_goodies, min_price_diff = calculate_goodies(lines)

      # Write the output to the output file
      with open(output_file, 'w') as file:
          file.write('The goodies selected for distribution are:\n')
          for name, price in selected_goodies:
              file.write(f'{name}: {price}\n')
          file.write(f'And the difference between the chosen goodie with highest price and the lowest price is {min_price_diff}')
    
    except FileNotFoundError:
        print("Input file not found")

    except Exception as e:
      print("Error: {}".format(e))
   

if __name__ == "__main__":
     main("sample_input.txt", "sample_output.txt")
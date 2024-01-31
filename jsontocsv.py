import pandas as pd

def remove_rows_starting_with(input_file, output_file, prefix='"'):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_file)

        # Remove entire rows where 'URL' column starts with the specified prefix
        df = df[~df['url'].str.startswith(prefix)]

        # Save the modified DataFrame to a new CSV file
        df.to_csv(output_file, index=False)

        print(f"CSV file '{output_file}' created successfully with rows starting with '{prefix}' removed.")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'input_file.csv' and 'output_removed.csv' with the actual file paths
remove_rows_starting_with('output_concatenated.csv', 'output_removed.csv')

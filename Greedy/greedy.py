import os

def optimize_photoshoot(products, staging_times, photoshoot_times):
    n = len(products)
    
    # Create a hash map with product as key and value containing staging_time, photoshoot_time, and difference
    product_info = {}
    for i in range(n):
        diff = float(staging_times[i]) - float(photoshoot_times[i])
        product_info[products[i]] = {"staging_time": staging_times[i], "photoshoot_time": photoshoot_times[i], "diff": diff}
    
    # Sort the hash map with difference value from decreasing to increasing order
    sorted_products = sorted(product_info.items(), key=lambda x: x[1]['diff'], reverse=False)

    # Calculate the total time to complete all photoshoots
    total_time = 0
    for i in range(n):
        total_time += sorted_products[i][1]['photoshoot_time']

    # Calculate idle time for Gopal
    initial_idle_time = sorted_products[0][1]['staging_time']
    idle_time = 0
    for i in range(1, n):
        staging_time = sorted_products[i][1]['staging_time']
        prev_photoshoot_time = sorted_products[i-1][1]['photoshoot_time']
        diff = staging_time - prev_photoshoot_time
        idle_time += diff

    if idle_time > 0:
        idle_time += initial_idle_time
    else:
        idle_time = initial_idle_time
    total_time = total_time + idle_time

    return sorted_products, total_time, idle_time


def validate_inputs(products, staging_times, photoshoot_times):
    """
    Args:-
        products: list
        staging_times: list
        photoshoot_times: list
    Returns:-
        Exception:- ValueError
    """
    if not (len(products) == len(photoshoot_times) == len(staging_times)):
        raise ValueError('MisMatch Values Found.')
    staging_times_res = list(filter(lambda x: x < 0, staging_times))
    photoshoot_times_res = list(filter(lambda x: x < 0, photoshoot_times))
    if any(staging_times_res) or any(photoshoot_times_res):
        raise ValueError('Incorrect values.')
    return True


def read_input(file_name):
    inputs = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            try:
                products = lines[i].split(':')[1].strip().split(' / ')
                staging_times = list(map(int, lines[i + 1].split(':')[1].strip().split(' / ')))
                photoshoot_times = list(map(int, lines[i + 2].split(':')[1].strip().split(' / ')))
                res = validate_inputs(products, staging_times, photoshoot_times)
                inputs.append((products, staging_times, photoshoot_times))
            except ValueError as ve:
                print(ve)
            except Exception as ex:
                print(ex)
            except Exception as ex:
                pass
    return inputs


def write_output(file_name, product_sequence, total_time, idle_time):
    with open(file_name, 'a') as file:
        file.write("Product Sequence: " + ", ".join(product_sequence) + "\n")
        file.write("Total time to complete photoshoot: " + str(total_time) + " minutes\n")
        file.write("Idle time for Gopal: " + str(idle_time) + " minutes\n")
        file.write("\n")  # Add a blank line to separate outputs


def main():
    input_file = "inputPS10.txt"
    output_file = "outputPS10.txt"
    if os.path.exists(output_file):
        os.remove(output_file)

    # Read inputs from file
    inputs = read_input(input_file)

    # Process each set of inputs and write corresponding output
    for idx, (products, staging_times, photoshoot_times) in enumerate(inputs):
        try:
            sorted_products, total_time, idle_time = optimize_photoshoot(products, staging_times, photoshoot_times)
            product_sequence = [product[0] for product in sorted_products]
            write_output(output_file, product_sequence, total_time, idle_time)
        except Exception as ex:
            pass

if __name__ == "__main__":
    main()

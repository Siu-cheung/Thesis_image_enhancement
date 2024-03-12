def create_image_subset(input_dir, output_dir, subset_size=100, random_seed=42):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set a random seed for reproducibility
    random.seed(random_seed)

    # List all files in the input directory
    files = os.listdir(input_dir)

    # Select a random subset of images
    subset = random.sample(files, min(subset_size, len(files)))

    # Copy the selected subset of images to the output directory
    for image in subset:
        source_path = os.path.join(input_dir, image)
        destination_path = os.path.join(output_dir, image)
        shutil.copyfile(source_path, destination_path)

    print(f"Subset of {len(subset)} images copied to '{output_dir}'")

    def calculate_histogram_statistics(image_dir):
    data = []

    for image_name in os.listdir(image_dir):
        # Read the image
        image_path = os.path.join(image_dir, image_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Calculate the histogram
        # hist = cv2.calcHist([image], [0], None, [256], [0,256])

        # Flatten the histogram
        # hist_flat = hist.flatten()

        # Calculate mean, standard deviation, min, max, and skewness
        mean = image.mean()
        std_dev = image.std()
        hist_min = image.min()
        hist_max = image.max()
        #skewness = image.mean((hist_flat - mean) ** 3) / (std_dev ** 3)

        # Append data to list
        data.append([image_name, mean, std_dev, hist_min, hist_max])

    # Create DataFrame
    df = pd.DataFrame(data, columns=['Image', 'Mean', 'Std Dev', 'Min', 'Max']) # ignoring Skewness for now
    return df
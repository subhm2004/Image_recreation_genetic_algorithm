# Evolving Images with Genetic Programming 🧬🖼️

This project implements a Genetic Programming (GP) algorithm to evolve images that resemble a target image. It leverages the power of evolutionary computation to generate artistic and visually appealing results. The core idea is to create a population of random images, evaluate their similarity to a target image, and then iteratively improve the population through selection, crossover, and mutation. This process mimics natural selection, where the "fittest" images (those most similar to the target) are more likely to reproduce and pass on their characteristics to the next generation.

## 🚀 Key Features

- **Image Evolution:** Employs a genetic algorithm to evolve images over generations, progressively refining them to resemble a target image.
- **Individual Representation:** Represents each candidate solution as an `Individual` object, which is essentially an image composed of randomly generated polygons.
- **Fitness Evaluation:** Calculates the fitness of each individual by comparing it to the target image using the Delta E (CIE76) color difference formula.
- **Parent Selection:** Uses tournament selection to choose parents for crossover, ensuring that fitter individuals have a higher chance of reproducing.
- **Crossover Operators:** Implements multiple crossover methods to combine the genetic material (image data) of two parent individuals, creating diverse offspring.
- **Mutation Operator:** Introduces random changes to the individuals' images by adding random shapes, promoting exploration of the solution space.
- **Data Tracking:** Stores the fitness data of the population over generations in a CSV file, enabling analysis and visualization of the algorithm's performance.
- **Visualization Tools:** Provides scripts to generate plots and GIF animations that visualize the evolution process.

## 🛠️ Tech Stack

*   **Programming Language:** Python
*   **Image Processing:**
    *   PIL (Pillow)
*   **Numerical Computation:** NumPy
*   **Data Analysis:** Pandas
*   **Plotting:** Matplotlib, Seaborn
*   **Color Calculations:** colour
*   **Animation:** glob, re
*   **Other:** math, random, IPython.display

## 📦 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

*   Python (3.6 or higher)
*   pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/subhm2004/Image_recreation_genetic_algorithm.git

    cd Image_recreation_genetic_algorithm

    ```

2.  Install the required packages:

    ```bash
    pip install numpy Pillow pandas matplotlib seaborn colour-science
    ```

### Running Locally

1.  Place your target image in the root directory of the project.
2.  Modify the `filename` variable in `GP.py` to point to your target image.
3.  Run the genetic programming algorithm:

    ```bash
    python GP.py
    ```

    Adjust `pop_size` and `epochs` in `GP.py` to control the population size and number of generations.

4.  (Optional) Generate the fitness plot:

    ```bash
    cd gif
    python create_graph.py
    cd ..
    ```

5.  (Optional) Create a GIF animation of the evolution process (ensure that the GP saves images during its run):

    ```bash
    cd gif
    python create_gif.py
    cd ..
    ```

## 💻 Project Structure

```
.
├── data_cross.csv
├── gif
│   ├── create_gif.py
│   └── create_graph.py
├── GP.py
├── Individual.py
└── README.md
```



## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests with bug fixes, new features, or improvements to the documentation.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

If you have any questions or suggestions, please feel free to contact me at [subhu04012003@gmail.com](mailto:subhu04012003@gmail.com).


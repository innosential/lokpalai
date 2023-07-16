# LokpalAI: The Indian Law Assistant for everyone

Welcome to the LokpalAI project repository! LokpalAI is an Indian Law Assistant that leverages the power of artificial intelligence to provide assistance and guidance in understanding and navigating the Indian legal system. This project aims to build and share an instruction-following Language Model (LLM) to make legal information more accessible and understandable to everyone.

## Repository Contents

This repository contains the following components:

1. **Data**: The `5k+` data used for fine-tuning the model is included in this repository. This dataset plays a crucial role in training the LokpalAI model, enabling it to understand and respond accurately to legal queries. The dataset is licensed under [CC BY NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), allowing only non-commercial use.

2. **Data Generation Code**: The code for generating the data used in fine-tuning the model is available in this repository. This code helps in creating and curating legal text samples that are essential for enhancing the performance and domain-specific knowledge of the LokpalAI model.

3. **Model Fine-tuning Code**: The code for fine-tuning the LokpalAI model can be found here. This code enables researchers and developers to train and fine-tune the model using custom datasets or specific legal domains to tailor the AI assistant according to their requirements.

4. **Weight Recovery Code**: The code for recovering Falcon-7B weights from our released weight diff is provided in this repository. This code facilitates the reconstruction of the model's weights based on the provided weight diff, enabling replication and further analysis of the model. The weight diff is licensed under [CC BY NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), allowing only non-commercial use.

## Model Versions

We have fine-tuned two versions of the LokpalAI model, and we are preparing to release their weights and the demo once we obtain the necessary permissions:

1. **MPT-7B**: This version of the model is fine-tuned on a large corpus of legal text using the MPT-7B architecture. It offers enhanced understanding and capabilities in Indian law-related tasks.

2. **Falcon-7B**: The Falcon-7B version of the LokpalAI model is fine-tuned on a diverse range of legal text using the Falcon-7B architecture. It provides robust performance and accuracy in addressing legal queries and assisting with legal tasks.

Stay tuned for the release of the weights and the demo of these models once the necessary permissions are obtained.

## Usage and License Notices

LokpalLLM is intended and licensed for research use only. The dataset used for training the model is licensed under [CC BY NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), allowing only non-commercial use. Therefore, any models trained using the dataset should not be used outside of research purposes.

The weight diff provided in this repository is also licensed under [CC BY NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), allowing only non-commercial use.

## Getting Started

To get started with LokpalAI, follow these steps:

1. Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/your-username/lokpalai.git
```
2. Install the necessary dependencies required for data generation, fine-tuning, or weight recovery. Refer to the README or documentation provided in the respective directories for detailed instructions.
3. Explore the `Data` directory to familiarize yourself with the dataset used for training the LokpalAI model. This dataset serves as a valuable resource for understanding the legal context and formulating relevant queries.
4. Use the data generation code provided in the repository to create custom legal text samples or modify existing ones to fine-tune the model for specific legal domains.
5. Fine-tune the LokpalAI model using the code available in the respective directory. Experiment with different hyperparameters, architectures, or datasets to achieve the desired performance and accuracy.
6. If you are interested in understanding the internals of the model and replicating its weights, utilize the weight recovery code provided in the repository. This code will help you reconstruct the model's weights based on the weight diff provided.

## Contributions and Feedback

We welcome contributions from the community to improve the LokpalAI project. If you would like to contribute, please follow the guidelines outlined in the CONTRIBUTING.md file.

If you encounter any issues, have suggestions, or want to provide feedback, please open an issue in the GitHub repository. We appreciate your participation and support in making LokpalAI a comprehensive and reliable Indian Law Assistant for everyone.

## License

The LokpalAI project is licensed under the [MIT License](LICENSE). Please review the license file for more details on permitted usage and distribution.

## Acknowledgments

We would like to express our gratitude to the contributors and the open-source community for their continuous support and efforts in developing and enhancing the LokpalAI project.

Special thanks to the Falcon-7B team for providing the released weight diff, which enables the recovery of the model's weights.

---

Thank you for your interest in LokpalAI! We hope this project helps in democratizing legal information and simplifying the understanding of the Indian legal system.

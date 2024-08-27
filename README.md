# Adaptive Gait Rehabilitation using Hybrid RL Algorithms

![pioneer](https://github.com/user-attachments/assets/70e7d3fb-154e-4238-9124-477f75084f8e)


This repository builds upon the research presented in the paper: [**Optimizing Policy Gradient Methods for Adaptive Gait Rehabilitation**](https://www.researchgate.net/publication/383177984_Optimizing_Policy_Gradient_Methods_for_Adaptive_Gait_Rehabilitation?channel=doi&linkId=66bfcb52145f4d35535fe3fa&showFulltext=true). (Preprint)

## Introduction

Adaptive gait rehabilitation is a critical field in medical research, aiming to improve mobility and quality of life for individuals with lower-limb disabilities. Traditionally, exoskeletons and other assistive devices have been used to support gait rehabilitation, but they require manual adjustments and lack adaptability. Reinforcement Learning (RL) has emerged as a promising approach to develop intelligent control systems for gait rehabilitation, allowing for real-time adjustments based on feedback from the environment.

This project introduces a hybrid approach that combines Convolutional Neural Networks (CNN) with Proximal Policy Optimization (PPO) and integrates genetic algorithms (Algae optimization). The objective is to develop a robust RL framework capable of learning and adapting to individual patient needs, ultimately leading to improved gait rehabilitation outcomes.

## Methodology

### Data Loading and Preprocessing

- **Datasets:** We utilized the OU-Biometrics dataset (OU-ISIR), specifically focusing on the TreadmillDatasetB and TreadmillDatasetD.
- **Preprocessing:** Input images were converted to tensors and normalized to ensure consistency when feeding data into the neural network.

### Convolutional Neural Network (CNN)

- **Architecture:** The model consists of convolutional layers, fully connected layers, and an output layer designed for the specific actions relevant to the dataset.
- **Dataset B:** Trained on a 3-layer CNN with ReLU activation, batch normalization, and max-pooling.
- **Dataset D:** Trained to analyze NAC (Normalized AutoCorrelation) values to detect gait abnormalities.

### Proximal Policy Optimization (PPO) + Algae Optimization

- **PPO:** Balances exploration and exploitation using a clipping mechanism to stabilize policy updates.
- **Algae Optimization:** Genetic algorithm-inspired method involving crossover and mutation operations to evolve neural network weights, enhancing robustness and adaptability.

### Training and Testing

- **Training Episodes:** 50 episodes for Dataset B and 10 episodes for Dataset D, considering data volume and complexity.
- **Evaluation:** Models were evaluated for fitness, with weights updated based on performance metrics like loss, optimizers, and evolution parameters.
- **Crossover and Mutation:** These genetic operations were applied every 5 episodes to introduce variability and evolve the model population.

## Experimental Results

### Dataset B

- **Training Loss:** Observed fluctuating training loss, but algae optimization effectively evolved better models.
- **Test Accuracy:** Achieved high accuracy (above 99%) after 50 episodes, demonstrating robust gait pattern segmentation.

### Dataset D

- **NAC Values:** The optimal shift value was found to be 69, with an NAC value close to 0.975, indicating a stable and consistent gait cycle.
- **Test Accuracy:** Consistently improving test accuracy across epochs, reaching perfect accuracy, with SHAP analysis providing insights into model decision-making.

## References

1. [The OU-ISIR Gait Database Comprising the Treadmill Dataset](https://git-disl.github.io/GTDLBench/datasets/mnist_datasets/)
2. [Reward-Adaptive Reinforcement Learning: Dynamic Policy Gradient Optimization for Bipedal Locomotion](https://arxiv.org/pdf/2107.01908.pdf)
3. [A Data-Driven Reinforcement Learning Solution Framework for Optimal and Adaptive Personalization of a Hip Exoskeleton](https://arxiv.org/ftp/arxiv/papers/2011/2011.06116.pdf)
4. [Static Standing Balance with Musculoskeletal Models Using PPO With Reward Shaping](https://tinyurl.com/mvktmf7z)
5. [A Novel Deep Reinforcement Learning Based Framework for Gait Adjustment](https://arxiv.org/pdf/2107.01908.pdf)
6. [Challenges with Reinforcement Learning in Prosthesis](https://www.mdpi.com/2227-7390/11/1/178)




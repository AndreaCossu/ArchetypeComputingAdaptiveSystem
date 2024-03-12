import os

import torch
import torchvision
from torch.utils.data import DataLoader
from torchvision import transforms


def get_mnist_data(
    root: os.PathLike, bs_train: int, bs_test: int, valid_perc: int = 10
):
    """Get the MNIST dataset and return the train, validation and test dataloaders.

    Args:
        root (os.PathLike): Path to the folder containing the MNIST dataset.
        bs_train (int): Batch size for the train dataloader.
        bs_test (int): Batch size for the validation and test dataloaders.
        valid_perc (int): Percentage of the train dataset to use for
            validation. Defaults to 10.
    """
    train_dataset = torchvision.datasets.MNIST(
        root=root, train=True, transform=transforms.ToTensor(), download=True
    )

    test_dataset = torchvision.datasets.MNIST(
        root=root, train=False, transform=transforms.ToTensor()
    )

    valid_size = int(len(train_dataset) * (valid_perc / 100.0))
    train_size = len(train_dataset) - valid_size
    train_dataset, valid_dataset = torch.utils.data.random_split(
        train_dataset, [train_size, valid_size]
    )

    train_loader = DataLoader(dataset=train_dataset, batch_size=bs_train, shuffle=True)
    valid_loader = DataLoader(dataset=valid_dataset, batch_size=bs_test, shuffle=False)
    test_loader = DataLoader(dataset=test_dataset, batch_size=bs_test, shuffle=False)

    return train_loader, valid_loader, test_loader

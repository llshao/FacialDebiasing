"""
In this file the evaluation of the network is done
"""

import torch
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("device:", DEVICE)

def run_epoch
    """
    perform evaluation of a single epoch
    """

    return

def main():

    return 

if __name__ == "__main__":
    print("start evaluation")

    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', default=40, type=int,
                        help='max number of epochs')
    parser.add_argument('--zdim', default=20, type=int,
                        help='dimensionality of latent space')

    ARGS = parser.parse_args()

    main()
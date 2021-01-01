import argparse


def getArgs(argv=None):
    parser = argparse.ArgumentParser(description='Default parameters of the models', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--batch_size', type=int, default=200, help='Size of the batches')
    parser.add_argument('--epochs', type=int, default=501, help='Number of epochs')
    parser.add_argument('--perp', type=int, default=10, help='Perplexity for the t-SNE')
#     parser.add_argument('--train', type=int, default=1, help='Training model flag')
    parser.add_argument('--train', action="store_true", help='Training model flag')
    parser.add_argument('--display', action='store_true', help='Display option flag')
    parser.add_argument('--save', type=int, default=1000, help='Save variables every save no. of iterations')
    parser.add_argument('--restore', type=int, default=0, choices=[0,1], help='To restore session, to keep training or evaluation')
    parser.add_argument('--plot', type=int, default=1, help='Plot results flag')
    parser.add_argument('--dim_latent_s',type=int, default=10, help='Dimension of the categorical space')
    parser.add_argument('--dim_latent_z',type=int, default=2, help='Dimension of the Z latent space')
    parser.add_argument('--dim_latent_y',type=int, default=10, help='Dimension of the Y latent space')
    parser.add_argument('--dim_latent_y_partition',type=int, nargs='+', help='Partition of the Y latent space') # nargs = +, inputs a list 
    parser.add_argument('--miss_percentage_train',type=float, default=0.0, help='Percentage of missing data in training')
    parser.add_argument('--miss_percentage_test',type=float, default=0.0, help='Percentage of missing data in test')
    parser.add_argument('--model_name', type=str, default='model_new', help='File of the training model')
    parser.add_argument('--save_file', type=str, default='new_mnist_zdim5_ydim10_4images_', help='Save file name')
    parser.add_argument('--data_file', type=str, default='MNIST_data', help='File with the data')
    parser.add_argument('--types_file', type=str, default='mnist_train_types2.csv', help='File with the types of the data')
    parser.add_argument('--miss_file', type=str, default='Missing_test.csv', help='File with the missing indexes mask')
    parser.add_argument('--true_miss_file', type=str, help='File with the missing indexes when there are NaN in the data')
    return parser.parse_args(argv)
    
    
class dotdict(dict):
    """dot notation access to dictionary attributes. Will not work for nested dictionaries."""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    
    
def getArgs_jupyter_notebook():
    params = dict()
    params['batch_size'] = 200
    params['epochs'] = 5
    params['perp'] = 10
    params['train'] = 1
    params['display'] = 1
    params['save'] = 1000
    params['restore'] = 0
    params['plot'] = 1
    params['dim_latent_s'] = 4
    params['dim_latent_z'] = 2
    params['dim_latent_y'] = 3 
    params['dim_latent_y_partition'] = []
    params['miss_perentage_train'] = 0.0
    params['miss_percentage_test'] = 0.0
    params['model_name'] = 'model_new'
    params['save_file'] = 'breast_data_zdim5_ydim10_4images_'
    params['data_file'] = './Breast/data.csv'
    params['types_file'] = './Breast/data_types.csv'
    params['miss_file'] = './Breast/Missing40_4.csv'
    params['true_miss_file'] = ''
    param_object = dotdict(params)
    return param_object

    
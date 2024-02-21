
from core.importer import importer



def grouped_parameters(file_path,chunk):
    """
    converts a list of parameters into parameter and value pair
    returns dict
    """
    with open(file_path, 'r') as f:
        params = [line.strip() for line in f.readlines()]
        parameters = [param + '="dalaho' for param in params]

        grouped_parameters = ['&'.join(parameters[i:i+chunk]) for i in range(0, len(parameters),chunk)]
        return grouped_parameters
       




def prepare_requests(args):
    """
    creates a list of request objects used by Arjun from targets given by user
    returns list (of targs)
    """
    
    if args.import_file:
        return importer(args.import_file)
    return []


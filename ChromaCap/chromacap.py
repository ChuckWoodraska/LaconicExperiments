import photomosaic as pm
from skimage.io import imread, imsave


def gen_pic():
    target = '28387.jpg'
    image = imread(target)
    dims_list = [(150, 150,), ]

    # Analyze the collection (the "pool") of images.
    # pool = pm.make_pool('guinnesscaps/*.jpg')
    # Generate a collection of solid-color square images.
    pm.rainbow_of_squares('pool/', range_params=(0, 256, 128))

    # Analyze the collection (the "pool") of images.
    pool = pm.make_pool('pool/*.png')
    for dims in dims_list:
        mos = pm.basic_mosaic(image, pool, dims, depth=1)
        imsave('mosaic_{}.png'.format(target), mos)


if __name__ == '__main__':
    gen_pic()

def read_bios(filename='data/day08.txt'):
    with open(filename) as f:
        data = f.read().strip()
    return data


def get_layers(bios, image_size):
    return [bios[i:i + image_size] for i in range(0, len(bios), image_size)]


def get_min_layer(layers):
    l = [layer.count('0') for layer in layers]
    min_layer = layers[l.index(min(l))]
    return min_layer.count('1') * min_layer.count('2')


if __name__ == '__main__':

    bios = read_bios()
    print(get_min_layer(get_layers(bios, 25 * 6)))


from PIL import Image
import os
import argparse

# to run this program
# python3 image_resize.py --input_dir=/Users/xxx/Pictures --output_dir=/Users/xxx/Pictures/resized
# python3 image_resize.py --input_dir=/Users/xxx/Pictures --output_dir=/Users/xxx/Pictures/resized --width=640 --height=640 --dpi=72


default_size = (1024,1024)
default_dpi =(300,300)

def resize_image(input_dir, infile, output_dir, size, dpi):
    outfile = os.path.splitext(infile)[0] + "_resized"
    extension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        img.thumbnail(size)

        new_file = output_dir + "/" + outfile + extension
        img.save(new_file, dpi=dpi)

    except IOError:
        print("unable to resize image {}".format(infile))


if __name__ == "__main__":
    curr_dir = os.getcwd()
    # print(curr_dir)
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_dir', help='Full input path')
    parser.add_argument('-o','--output_dir', help='Full output path')
    parser.add_argument('-w','--width', help='Resize width')
    parser.add_argument('-t','--height', help='Resize height')
    parser.add_argument('-d','--dpi', help='Resolution')
    
    args = parser.parse_args()
    # print(args)
    
    if args.input_dir:
        input_dir = args.input_dir
    else:
        input_dir = curr_dir + '/images'

    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = curr_dir + '/resized'  

    if args.dpi:
        dpi = (int(args.dpi), int(args.dpi))
    else:
        dpi = default_dpi    

    if args.width and args.height:
        size = (int(args.width), int(args.height))
    else:
        size = default_size
        
    if not os.path.exists(os.path.join(curr_dir, output_dir)):
        os.mkdir(output_dir)  
        
    try:
        for file in os.listdir(input_dir):
            filename, ext = os.path.splitext(file)
            if ext == ".jpg" :
               resize_image(input_dir, file, output_dir, size=size, dpi=dpi)
    except OSError:
        print('file not found')          
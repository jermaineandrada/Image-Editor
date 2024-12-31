
# ID# 3143804
# Lab 7 CMPT 103 Assignment


from graphics import *
import tkinter as tk
from tkinter import filedialog


def button_(win, position, label):
    """
        Purpose: 
        This creates a button
        
    
        Parameters:
        win (no type) - win is just GraphWin()
        posistion (int)
        label (string)
        
        Returns:
        button - draws the button
        (10, position + 10, 110, position + 60) - tuple, coordinates of the button
        
        
        Note: all of the returns are Point() 

    
    """     
    top_left = Point(10, 10)
    bottom_right = Point(110, 60)

    button = Rectangle(top_left, bottom_right)
    button.move(0, position)
    button.draw(win)
    
    label_text = Text(Point(60, 35 + position), label)
    label_text.draw(win)
    
    # returns the drawing of the rectangle
    # and the coordinates in the format (x1, y1, x2, y2)
    return button, (10, position + 10, 110, position + 60)

def get_image_click_coords(win, img):
    """
        Purpose: 
        gets the points of user's click in the targeted image
        
    
        Parameters:
        win (no type) - win is just GraphWin()
        img (no type) - an actual image
        
        Returns:
        x
        y
        x_img
        y_img
        
        Note: all of the returns are Point() 

    
    """    
    click_point = win.getMouse()
    x, y = click_point.getX(), click_point.getY()
    

    # Calculate image's top-left corner based on anchor point and dimensions
    img_top_left_x = img.anchor.getX() - img.getWidth() / 2
    img_top_left_y = img.anchor.getY() - img.getHeight() / 2

    # Translate window click coordinates to image pixel coordinates
    x_img = int(x - img_top_left_x)
    y_img = int(y - img_top_left_y)
    
    # Print the pixel coordinates
    
    
    # Return coordinates
    return x, y, x_img, y_img    


def convert_grayscale(img, point1, point2):
    """
        Purpose: 
        converts the selected area to a gray scale
        
    
        Parameters:
        img (no type) -> an actual image
        point1 (no type) -> Point()
        point2 (no type) -> Point()
    
        Returns:
        None

    
    """     
    x1, y1 = int(point1.getX()), int(point1.getY())
    x2, y2 = int(point2.getX()), int(point2.getY())
    
   
    # Apply grayscale
    for x in range(x1, x2):
        for y in range(y1, y2):
            r, g, b = img.getPixel(x, y)  # Get pixel's RGB values
            
            # Greyscale calculation
            grey = int(0.299 * r + 0.587 * g + 0.114 * b)
            
            # Instead of setPixel, use plot (if available)
            
                     
            img.setPixel(x, y, color_rgb(grey, grey, grey))
            
def convert_negative(img, point1, point2):
    """
        Purpose: 
        converts the selected area to a negative rgb
        
    
        Parameters:
        img (no type) -> an actual image
        point1 (no type) -> Point()
        point2 (no type) -> Point()
    
        Returns:
        None

    
    """      
    x1, y1 = int(point1.getX()), int(point1.getY())
    x2, y2 = int(point2.getX()), int(point2.getY())
    
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            r, g, b = img.getPixel(x, y)  # Get pixel's RGB values
            neg_r = 255 - r
            neg_g = 255 - g
            neg_b = 255 - b            
            img.setPixel(x, y, color_rgb(neg_r, neg_g, neg_b))
            
            
                     
def open_file_dialog(win):
    """
        Purpose: 
        Opens up the file dialog, prompts the user to chose a file
        
    
        Parameters:
        win (no type)
    
        Returns:
        img
        None

    
    """      
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"File selected: {file_path}")
        # just to clarify what file was selected
    root.destroy()
    
    if file_path:
        img = Image(Point(309.0, 184.5), file_path)  # Center the image in the window
        img.draw(win) 
        
        return img
    return None
    

# if a button is clicked within boundaries then this verify it is within range
# relative to its ranges
def button_chosen(button_bounds, click_point):
    """
        Purpose: 
        Verifys if a click is within the boundaries of the button
    
        Parameters:
        button_bounds (tuple)
        click_point (no type) -> click_point is win.getMouse() 
    
        Returns:
        x1 <= click_point.getX() <= x2 and y1 <= click_point.getY() <= y2
        
        returns the x and y range, each button has their own specific ranges

    
    """     
    x1, y1, x2, y2 = button_bounds
    return x1 <= click_point.getX() <= x2 and y1 <= click_point.getY() <= y2



def save_image(image):
    """
        Purpose: 
        Prompts the user a location to save a file
    
        Parameters:
        - image 
        
        Doesn't have a parameter type since the parameter is an image
    
        Returns:
        None
    
    """       
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        image.save(file_path)  
        # Save the image if a file path was selected   

def main():
    """
        Purpose: 
        Creates a window, display area and calls upon the other helper functions
    
        Parameters:
        None
    
        Returns:
        None
    
    """    
    
     # creates the overall window
    win = GraphWin('CMPT103 Fall 2024 - Assignment 7', 500, 370)
    display_area = Rectangle(Point(110, 0), Point(490, 369))
    display_area.draw(win)
    display_area.move(9, 0) 
    
    button, load_bounds = button_(win, 0, 'Load')
    button, select_bounds = button_(win, 60, 'Select')
    button, gray_bounds = button_(win, 120, 'Grayscale')
    button, negative_bounds = button_(win, 180, 'Negative')
    button, save_bounds = button_(win, 240, 'Save')
    button, quit_bounds = button_(win, 300, 'Quit')
    
    while True:
        click_point = win.getMouse()
        # the click_point is essential for telling us where the user clicked
        # if click is within a button then it will perform that function
        if button_chosen(load_bounds, click_point):
            print("Load button clicked!")
            # to verify that select button has been clicked
            # if within range, it should open up the file dialog to choose image
            img = open_file_dialog(win)    
        elif button_chosen(select_bounds, click_point):
            print('Select button clicked!')
            
            x1, y1, x1_img, y1_img     = get_image_click_coords(win, img)
            print(f'({x1}, {y1} and {x1_img}, {y1_img})')
            image_p1 = Point(x1_img, y1_img)
            
            x2, y2, x2_img, y2_img    = get_image_click_coords(win, img)
            print(f'({x2}, {y2} and {x2_img}, {y2_img})')
            image_p2 = Point(x2_img, y2_img)
            # essentially, it gets the coords of two things
            # 1. the two selected points of the window
            # 2. the two selected points of the image (assuming the user targets it)
            selected_area = Rectangle(Point(x1,y1), Point(x2, y2))
            # we create a rectangle as a display with the points of the window
            # we use the points of the selected pixels to convert to a gray scale or a negative rgb
            selected_area.draw(win)
            
        elif button_chosen(gray_bounds, click_point):
            print('Grayscale button clicked!')
            if img:
                convert_grayscale(img, image_p1, image_p2)
        elif button_chosen(negative_bounds, click_point):
            print('Negative button clicked!')
            if img:
                convert_negative(img, image_p1, image_p2)
        elif button_chosen(save_bounds, click_point):
            print('Save button clicked!')
            save_image(img)
        elif button_chosen(quit_bounds, click_point):
            win.close()
            break
            
            
main()          
            
        
            
            
             
        


            



    

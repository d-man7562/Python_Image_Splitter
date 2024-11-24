from PIL import Image
import os

def split_spritesheet(input_path, output_folder, num_frames, output_prefix="frame"):
    """
    Split a horizontal sprite sheet into individual frames while preserving transparency.
    
    Args:
        input_path (str): Path to the input sprite sheet
        output_folder (str): Folder to save the individual frames
        num_frames (int): Number of frames in the sprite sheet
        output_prefix (str): Prefix for output filenames
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the sprite sheet
    sprite_sheet = Image.open(input_path)
    
    # Ensure the image has an alpha channel
    if sprite_sheet.mode != 'RGBA':
        sprite_sheet = sprite_sheet.convert('RGBA')
    
    # Calculate frame width
    frame_width = sprite_sheet.width // num_frames
    frame_height = sprite_sheet.height
    
    # Split and save each frame
    for i in range(num_frames):
        # Calculate frame boundaries
        left = i * frame_width
        top = 0
        right = (i + 1) * frame_width
        bottom = frame_height
        
        # Extract frame
        frame = sprite_sheet.crop((left, top, right, bottom))
        
        # Save frame with transparency
        output_path = os.path.join(output_folder, f"{output_prefix}_{i}.png")
        frame.save(output_path, "PNG")
        print(f"Saved frame {i + 1} to {output_path}")

# Example usage
if __name__ == "__main__":
    input_path = "Desktop/Greek_game_sprite_WIP.png"  # Replace with your sprite sheet path
    output_folder = "split_frames"   # Output folder name
    num_frames = 6                   # Number of frames in your sprite sheet
    
    split_spritesheet(input_path, output_folder, num_frames)
import cv2 



def drawfacebox_emotions(frame , em_dict ):
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7

    # Red color for the text (BGR format)
    text_color = (0, 0, 255)

    # White color for the background (optional, for better readability with dark backgrounds)
    background_color = (255, 255, 255)  # White in BGR

    thickness = 2

    # Calculate text position (above the top line)
    
    for k in range(len(em_dict)):
    
        text = em_dict[k]  # Replace with your desired text
        text_width, _ = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_height = int(font_scale * 35)  # Approximate text height
        text_x = 10  # Add some padding from the left border
        text_y = 25 * (k + 1) + 15
        # Define black background region with padding
        background_offset_x, background_offset_y = 3, 3  # Adjust padding as needed
        background_width = text_width + thickness * 2 + background_offset_x * 2
        background_height = text_height + thickness + background_offset_y * 2

        background_region = (text_x - background_offset_x, text_y - background_offset_y - background_height,
                            background_width, background_height)

        # Draw black rectangle
        cv2.rectangle(frame, background_region, (0, 0, 0), cv2.FILLED)
    
    covered = 0
    
    for k in range(len(em_dict)):
        
        text = em_dict[k]  # Replace with your desired text
        text_width, _ = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_height = int(font_scale * 35)  # Approximate text height
        text_x = 10  # Add some padding from the left border
        text_y = 25 * (k + 1) + 15
        covered += text_y 
        # Define black background region with padding
        background_offset_x, background_offset_y = 3, 3  # Adjust padding as needed
        background_width = text_width + thickness * 2 + background_offset_x * 2
        background_height = text_height + thickness + background_offset_y * 2

        background_region = (text_x - background_offset_x, text_y - background_offset_y - background_height,
                            background_width, background_height)
        cv2.putText(frame, text, (text_x , text_y - 10 ), font, font_scale, text_color, thickness)
    return covered

def drawfacebox_hoi(frame , hoi_dict , coverd = 0):

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7

    # Red color for the text (BGR format)
    text_color = (0, 0, 255)

    # White color for the background (optional, for better readability with dark backgrounds)
    background_color = (255, 255, 255)  # White in BGR

    thickness = 2

    # Calculate text position (above the top line)
    
    for k in range(len(hoi_dict)):
        
        text = ""
        for j in hoi_dict[k]:
            text+=" " + str(j) + " "
        
        text_width, _ = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_height = int(font_scale * 35)  # Approximate text height
        text_x = 10  # Add some padding from the left border
        text_y = coverd + 25 * (k+1) + 15
        # Define black background region with padding
        background_offset_x, background_offset_y = 3, 3  # Adjust padding as needed
        background_width = text_width + thickness * 2 + background_offset_x * 2
        background_height = text_height + thickness + background_offset_y * 2

        background_region = (text_x - background_offset_x, text_y - background_offset_y - background_height,
                            background_width, background_height)

        # Draw black rectangle
        cv2.rectangle(frame, background_region, (0, 0, 0), cv2.FILLED)
    
    for k in range(len(hoi_dict)):
        
        text = ""
        for j in hoi_dict[k]:
            text+=" " + str(j) + " "
            
        text_width, _ = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_height = int(font_scale * 35)  # Approximate text height
        text_x = 10  # Add some padding from the left border
        text_y = coverd + 25 * (k+1) + 15
        # Define black background region with padding
        background_offset_x, background_offset_y = 3, 3  # Adjust padding as needed
        background_width = text_width + thickness * 2 + background_offset_x * 2
        background_height = text_height + thickness + background_offset_y * 2

        background_region = (text_x - background_offset_x, text_y - background_offset_y - background_height,
                            background_width, background_height)
        cv2.putText(frame, text, (text_x , text_y - 10 ), font, font_scale, text_color, thickness)

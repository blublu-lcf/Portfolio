import os
import re
import shutil
from typing import Dict

# Define the root directory of your project
root_dir = './'

# Define the new directory structure
new_structure = {
    'assets/css': [],
    'assets/js': [],
    'assets/fonts': [],
    'assets/images/png': [],
    'assets/videos': [],
    'assets/downloads': [],
    'pages': [],
}

# Define the mapping of old file names to new file names in kebab-case
file_mapping = {
    # HTML files
    'Home.html': 'index.html',  # Special case for the home page
    'Control.html': 'control.html',
    'Film.html': 'film.html',
    'Game.html': 'game.html',
    'Gourmet Flow.html': 'gourmet-flow.html',
    'GrannyBlue.html': 'granny-blue.html',
    'Gravity.html': 'gravity.html',
    'Interaction_Design.html': 'interaction-design.html',
    'Other_Works.html': 'other-works.html',
    'Rose&Palette.html': 'rose-and-palette.html',

    # CSS files
    'Home.css': 'home.css',
    'Film.css': 'film.css',
    'Game.css': 'game.css',
    'Gourmet Flow.css': 'gourmet-flow.css',
    'GrannyBlue.css': 'granny-blue.css',
    'Gravity.css': 'gravity.css',
    'Interaction_Design.css': 'interaction-design.css',
    'Other_Works.css': 'other-works.css',
    'Rose&Palette.css': 'rose-and-palette.css',

    # JS files
    'Home.js': 'home.js',
    'Film.js': 'film.js',
    'Game.js': 'game.js',
    'Gourmet Flow.js': 'gourmet-flow.js',
    'GrannyBlue.js': 'granny-blue.js',
    'Gravity.js': 'gravity.js',
    'Interaction_Design.js': 'interaction-design.js',
    'Other_Works.js': 'other-works.js',
    'Rose&Palette.js': 'rose-and-palette.js',

    # Font files
    'americantypewriterbold.ttf': 'americantypewriterbold.ttf',  # No change needed

    # Video files
    'Bank.mp4': 'bank.mp4',
    'Choice.mp4': 'choice.mp4',
    'Dungeon.mp4': 'dungeon.mp4',
    'GrannyBlue.mp4': 'granny-blue.mp4',
    'Moon.mp4': 'moon.mp4',
    'Night.mp4': 'night.mp4',
    'Ticket.mp4': 'ticket.mp4',
    'trailer.mp4': 'trailer.mp4',

    # Zip file
    'Rose&Palette.zip': 'rose-and-palette.zip',

    # PNG files
    '1.png': '1.png',  # No change needed
    '2.png': '2.png',  # No change needed
    '3.png': '3.png',  # No change needed
    '4.png': '4.png',  # No change needed
    'Bank.png': 'bank.png',
    'Character.png': 'character.png',
    'Choice.png': 'choice.png',
    'Control.png': 'control.png',
    'Dream.png': 'dream.png',
    'Dungeon.png': 'dungeon.png',
    'Frame 6.png': 'frame-6.png',
    'GF.png': 'gf.png',
    'Game.png': 'game.png',
    'GameUI.png': 'game-ui.png',
    'Goodnight.png': 'goodnight.png',
    'GourmetFlow.png': 'gourmet-flow.png',
    'GourmetMusic.png': 'gourmet-music.png',
    'GourmetSceneDesign.png': 'gourmet-scene-design.png',
    'GourmetTitle.png': 'gourmet-title.png',
    'Granny.png': 'granny.png',
    'GrannyBlueScreenshot.png': 'granny-blue-screenshot.png',
    'GrannyBlueTitle.png': 'granny-blue-title.png',
    'GravicamExperience.png': 'gravicam-experience.png',
    'GravicamFace.png': 'gravicam-face.png',
    'GravicamInstallation.png': 'gravicam-installation.png',
    'GravicamTitle.png': 'gravicam-title.png',
    'GravicamUI.png': 'gravicam-ui.png',
    'Gravity.png': 'gravity.png',
    'Heal.png': 'heal.png',
    'Interstellar.png': 'interstellar.png',
    'LC.png': 'lc.png',
    'Layer_1.png': 'layer-1.png',
    'Layer_3.png': 'layer-3.png',
    'Lens.png': 'lens.png',
    'Moon.png': 'moon.png',
    'Night.png': 'night.png',
    'OtherWorks.png': 'other-works.png',
    'Pacify.png': 'pacify.png',
    'Rose.png': 'rose.png',
    'RoseScreen.png': 'rose-screen.png',
    'RoseTitle.png': 'rose-title.png',
    'Ticket.png': 'ticket.png',
    'Torn Paper Mockup 01 1.png': 'torn-paper-mockup-01-1.png',
    'Torn Paper Mockup 13 1.png': 'torn-paper-mockup-13-1.png',
    'a.png': 'a.png',  # No change needed
    'arrow.png': 'arrow.png',  # No change needed
    'arrow1.png': 'arrow1.png',  # No change needed
    'awkward.png': 'awkward.png',  # No change needed
    'bg1.png': 'bg1.png',  # No change needed
    'bottom.png': 'bottom.png',  # No change needed
    'bubble.png': 'bubble.png',  # No change needed
    'circle.png': 'circle.png',  # No change needed
    'connect.png': 'connect.png',  # No change needed
    'connect1.png': 'connect1.png',  # No change needed
    'crown.png': 'crown.png',  # No change needed
    'designer.png': 'designer.png',  # No change needed
    'diamond.png': 'diamond.png',  # No change needed
    'flash.png': 'flash.png',  # No change needed
    'heart.png': 'heart.png',  # No change needed
    'infinite.png': 'infinite.png',  # No change needed
    'parallel.png': 'parallel.png',  # No change needed
    'pencil.png': 'pencil.png',  # No change needed
    'plus.png': 'plus.png',  # No change needed
    'portrait.png': 'portrait.png',  # No change needed
    'question.png': 'question.png',  # No change needed
    'rational.png': 'rational.png',  # No change needed
    'river.png': 'river.png',  # No change needed
    'river1.png': 'river1.png',  # No change needed
    'river2.png': 'river2.png',  # No change needed
    'smile.png': 'smile.png',  # No change needed
    'spider.png': 'spider.png',  # No change needed
    'star.png': 'star.png',  # No change needed
    'storm.png': 'storm.png',  # No change needed
    'thinking.png': 'thinking.png',  # No change needed
    'tree.png': 'tree.png',  # No change needed
}

# Function to create the new directory structure
def create_structure(root_dir, new_structure):
    for directory in new_structure:
        os.makedirs(os.path.join(root_dir, directory), exist_ok=True)
        print(f'Created directory: {directory}')

# Function to move files to their new locations
def move_files(root_dir, new_structure):
    # Move CSS files to assets/css
    for file in os.listdir(root_dir):
        if file.endswith('.css'):
            shutil.move(os.path.join(root_dir, file), os.path.join(root_dir, 'assets/css', file))
            print(f'Moved {file} to assets/css')

    # Move JS files to assets/js
    for file in os.listdir(root_dir):
        if file.endswith('.js'):
            shutil.move(os.path.join(root_dir, file), os.path.join(root_dir, 'assets/js', file))
            print(f'Moved {file} to assets/js')

    # Move font files to assets/fonts
    if os.path.exists(os.path.join(root_dir, 'Font')):
        for file in os.listdir(os.path.join(root_dir, 'Font')):
            shutil.move(os.path.join(root_dir, 'Font', file), os.path.join(root_dir, 'assets/fonts', file))
            print(f'Moved {file} to assets/fonts')
        os.rmdir(os.path.join(root_dir, 'Font'))

    # Move PNG files to assets/images/png
    if os.path.exists(os.path.join(root_dir, 'PNG')):
        for file in os.listdir(os.path.join(root_dir, 'PNG')):
            shutil.move(os.path.join(root_dir, 'PNG', file), os.path.join(root_dir, 'assets/images/png', file))
            print(f'Moved {file} to assets/images/png')
        os.rmdir(os.path.join(root_dir, 'PNG'))

    # Move video files to assets/videos
    if os.path.exists(os.path.join(root_dir, 'Video')):
        for file in os.listdir(os.path.join(root_dir, 'Video')):
            shutil.move(os.path.join(root_dir, 'Video', file), os.path.join(root_dir, 'assets/videos', file))
            print(f'Moved {file} to assets/videos')
        os.rmdir(os.path.join(root_dir, 'Video'))

    # Move HTML files to pages
    for file in os.listdir(root_dir):
        if file.endswith('.html'):
            shutil.move(os.path.join(root_dir, file), os.path.join(root_dir, 'pages', file))
            print(f'Moved {file} to pages')

    # Move the zip file to file
    if os.path.exists(os.path.join(root_dir, 'File')):
        shutil.move(os.path.join(root_dir, 'File', 'Rose&Palette.zip'), os.path.join(root_dir, 'assets/downloads', 'Rose&Palette.zip'))
        print(f'Moved Rose&Palette.zip to file')

# Function to update file paths and names in HTML, CSS, and JS files
def update_references(root_dir: str, file_mapping: Dict[str, str]):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if filename.endswith(('.html', '.css', '.js')):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Update file paths and names
                for old_name, new_name in file_mapping.items():
                    # Update CSS references
                    if old_name.endswith('.css'):
                        content = re.sub(
                            rf'href="([^"]*{re.escape(old_name)})"',
                            rf'href="/assets/css/{new_name}"',
                            content
                        )
                    # Update JS references
                    elif old_name.endswith('.js'):
                        content = re.sub(
                            rf'src="([^"]*{re.escape(old_name)})"',
                            rf'src="/assets/js/{new_name}"',
                            content
                        )
                    # Update HTML references
                    elif old_name.endswith('.html'):
                        content = re.sub(
                            rf'href="([^"]*{re.escape(old_name)})"',
                            rf'href="/pages/{new_name}"',
                            content
                        )
                    # Update PNG references
                    elif old_name.endswith('.png'):
                        content = re.sub(
                            rf'src="([^"]*{re.escape(old_name)})"',
                            rf'src="/assets/images/png/{new_name}"',
                            content
                        )
                    # Update MP4 references
                    elif old_name.endswith('.mp4'):
                        content = re.sub(
                            rf'src="([^"]*{re.escape(old_name)})"',
                            rf'src="/assets/videos/{new_name}"',
                            content
                        )

                    # Update MP4 references
                    elif old_name.endswith('.zip'):
                        content = re.sub(
                            rf'href="([^"]*{re.escape(old_name)})"',
                            rf'href="/assets/downloads/{new_name}"',
                            content
                        )

                    elif old_name.endswith('.ttf'):
                        content = re.sub(
                            rf"url('([^']*{re.escape(old_name)})')",
                            rf"url('/assets/fonts/{new_name}')",
                            content
                        )
                        
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f'Updated references in {filename}')


# Function to rename files and update references
def refactor_project(root_dir, file_mapping):
    # First, rename the files
    for old_name, new_name in file_mapping.items():
        # Handle files in the root directory
        old_path = os.path.join(root_dir, old_name)
        new_path = os.path.join(root_dir, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f'Renamed {old_name} to {new_name}')

        # Handle files in subdirectories
        for subdir in ['assets/css', 'assets/js', 'assets/fonts', 'assets/images/png', 'assets/videos', 'assets/downloads', 'pages']:
            old_path = os.path.join(root_dir, subdir, old_name)
            new_path = os.path.join(root_dir, subdir, new_name)
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f'Renamed {old_name} to {new_name} in {subdir}')

    # Now, update references in the files
    update_references(root_dir, file_mapping)

# Main function to refactor the project
def main():
    # Create the new directory structure
    create_structure(root_dir, new_structure)

    # Move files to their new locations
    move_files(root_dir, new_structure)

    # Refactor file names and update references
    refactor_project(root_dir, file_mapping)

    print('Project structure refactored successfully!')

# Run the script
main()

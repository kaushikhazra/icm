#!/usr/bin/env python3
import os
import shutil
import sys
import argparse
from pathlib import Path

def copy_claude_folders(target_folder):
    """Copy configured .claude folders to target folder"""
    
    # List of folders to copy from .claude directory
    folders_to_copy = [
        "commands",
        "agents"
    ]
    
    # Get the current directory (where this script is located)
    current_dir = Path(__file__).parent
    
    # Convert target to Path object
    target_path = Path(target_folder)
    
    # Check if target folder exists, create if it doesn't
    if not target_path.exists():
        try:
            target_path.mkdir(parents=True, exist_ok=True)
            print(f"Created target directory: {target_path}")
        except Exception as e:
            print(f"Error creating target directory: {e}")
            return False
    
    # Define destination .claude directory
    claude_dest = target_path / ".claude"
    
    try:
        # Create .claude directory in target if it doesn't exist
        claude_dest.mkdir(exist_ok=True)
        
        # Iterate through folders and copy each one
        for folder_name in folders_to_copy:
            src_folder = current_dir / ".claude" / folder_name
            dest_folder = claude_dest / folder_name
            
            if src_folder.exists():
                # Remove existing destination folder if it exists
                if dest_folder.exists():
                    shutil.rmtree(dest_folder)
                
                # Copy the folder
                shutil.copytree(src_folder, dest_folder)
                print(f"Copied .claude/{folder_name} to {dest_folder}")
            else:
                print(f"Warning: {src_folder} not found")
        
        return True
        
    except Exception as e:
        print(f"Error copying folders: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Copy .claude/command and .claude/agent folders to a target directory")
    parser.add_argument("target_folder", help="Target folder to copy .claude folders to")
    
    args = parser.parse_args()
    
    if not args.target_folder:
        print("Error: Please provide a target folder")
        sys.exit(1)
    
    success = copy_claude_folders(args.target_folder)
    
    if success:
        print("Setup completed successfully!")
        sys.exit(0)
    else:
        print("Setup failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
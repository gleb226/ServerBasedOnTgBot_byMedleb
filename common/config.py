folders = {
    "Photos": {
        "path": "photos",
        "subcategories": ["Egypt", "Budapest", "Prague", "School Trips", "Watches", "Diving", "Skiing", "Cat", "Amelia", "Other"]
    },
    "Videos": {
        "path": "videos",
        "subcategories": ["Egypt", "Budapest", "Prague", "School Trips", "Watches", "Diving", "Skiing", "Cat", "Amelia", "Other"]
    },
    "Documents": "documents",
    "Music": "music",
    "Python": "Python Files",
    "Passwords": "passwords",
    "Contacts": "contacts"
}

max_file_sizes = {
    "Photos": 20 * 1024 * 1024,
    "Videos": 50 * 1024 * 1024,
    "Documents": 50 * 1024 * 1024,
    "Music": 50 * 1024 * 1024,
    "Python": 50 * 1024 * 1024,
    "Passwords": 50 * 1024 * 1024,
    "Contacts": 50 * 1024 * 1024
}

file_extensions = {
    "Photos": ["jpg", "jpeg", "png", "gif", "bmp", "tiff"],
    "Videos": ["mp4", "mkv", "avi", "mov", "wmv", "flv"],
    "Music": ["mp3", "wav", "flac", "aac", "ogg"],
    "Documents": ["pdf", "docx", "txt", "xlsx", "pptx"],
    "Python": ["py"],
    "Passwords": ["txt", "csv"],
    "Contacts": ["vcf", "txt"]
}

translations = {
    "English": {
        "welcome": "Welcome! Please select a category.",
        "select_subcategory": "Select a subcategory:",
        "send_file": "Please send a {}.",
        "file_too_large": "The file is too large. Please send a smaller file.",
        "file_saved": "{} has been saved successfully!",
        "folder_error": "Invalid folder selected. Please try again."
    }
}

user_selections = {}

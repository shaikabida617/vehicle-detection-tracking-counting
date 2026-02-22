Computer Vision Detection Project
 
 Project Overview

This project is a real-time **Vehicle Detection, Tracking, and Counting System** built using Python and Computer Vision techniques.  
It detects vehicles from video input, tracks their movement across frames, and counts the total number of vehicles passing through a defined area.

This project demonstrates practical implementation of **Object Detection** and **Multi-Object Tracking** concepts.



Technologies Used

- Python  
- OpenCV  
- YOLO (You Only Look Once)  
- NumPy  
- SORT Tracking Algorithm  

 Project Structure

vehicle-detection-tracking-counting/
│
├── input/              # Input video files
├── models/             # YOLO model weights & config files
├── src/                # Main source code
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md

Installation & Setup

1. Clone the Repository

```bash
git clone https://github.com/shaikabida617/vehicle-detection-tracking-counting.git
cd vehicle-detection-tracking-counting

2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. How to Run the Project

```bash
python src/main.py
```

### Make sure:

- Input video is placed inside the `input` folder  
- YOLO model files are placed inside the `models` folder  

 Features

✔ Real-time vehicle detection  
✔ Multi-object tracking  
✔ Vehicle counting system  
✔ Clean modular project structure  
✔ Easy to modify and extend  


1. The system reads video input frame by frame.  
2. YOLO model detects vehicles in each frame.  
3. Tracking algorithm assigns unique IDs to vehicles.  
4. Vehicles crossing a predefined line are counted.  
5. Total vehicle count is displayed in real-time.  

 Applications

- Smart traffic management  
- Traffic flow analysis  
- Toll booth automation  
- Smart city surveillance systems  

 Future Improvements

- Add graphical user interface (GUI)  
- Deploy using Streamlit or Flask  
- Add vehicle speed estimation  
- Improve detection accuracy with custom-trained model  

 Developed By

**Shaik Abida**  
B.Tech CSE (Data Science) Student  
Passionate about AI, Computer Vision & Real-world Problem Solving  

---

⭐ If you found this project useful, consider giving it a star on GitHub!

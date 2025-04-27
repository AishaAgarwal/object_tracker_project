<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<div align="center">


</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
      </a>

  <h3 align="center">Real-Time Object Detection and Tracking</h3>

  <p align="center">

  
 

  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

  
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
<!--       <ul>
        <li><a href="#built-with">Project Structure</a></li>
      </ul> -->
    </li>
    <li><a href="#built-with">Project Structure</a></li>
    <li><a href="#design-decision-and-architechtural-considerations">Setup Instructions</a></li>
    <li><a href="#getting-started">Run using docker</a></li>
    <li><a href="#scaling-strategies">Techniques Used</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project


This project focuses on real-time video analytics to detect:

* New Object Placement: When a new object appears in the video scene.
* Missing Object Detection: When a previously detected object disappears from the scene.
  
The system uses a custom object detector and a tracker to assign unique IDs to objects and monitor their presence across frames. It is optimized for both detection accuracy and real-time performance (FPS).
Additional features include:
* Real-time bounding box drawing with object IDs.
* FPS calculation and live display on frames.
* Dockerized setup for easy deployment.
* Output video generation for analysis and submission.


## Project Structure


* src/ : Contains modular code for detection and tracking.
* videos/ : Store input test videos here.
* output/ : Stores the processed video with bounding boxes and FPS information.
* Dockerfile : Used to build the project inside a container.
* requirements.txt : List of required Python packages.


<!-- GETTING STARTED -->
## Setup Instructions

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

<h2> Prerequisites</h2>

1. Docker: To build and run the containerized environment.
2. Git: To clone the repository and track code changes.
3. Python 3.10 or higher: Required to run the project in case you wish to run it without Docker (optional).

<h2> Installation </h2>

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Navigate to the project directory
   ```sh
   cd <directory name>
3. Build the docker image 
   ```sh
   docker build -t object_tracker .
   ```
4. Run the docker container
   ```py
    docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix object_tracker
   ```
5. Running the project without Docker 
   ```py
   pip install -r requirements.txt
   python main.py
   ```
   
6. The project will automatically start processing the video, and you will see real-time object detection, tracking, and FPS calculation displayed in the video. The output will show new object detections, missing objects, and FPS on each frame.

7. You can replace the video file path in the main.py with your own video file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Techniques Used

* Object Detection :
   - **Model Choice**: The project uses a custom detector that can be implemented using pre-trained models like YOLO (You Only Look Once) or SSD (Single Shot Multibox Detector), or it can be built using a lightweight model for real-time inference.
   - **Detection Pipeline**: The detection process is optimized to identify objects within each video frame and generate bounding boxes around the detected objects.
* Object Tracking :
   - **Tracker Choice**: A tracking algorithm such as **Deep SORT** (Simple Online and Realtime Tracking) or **Kalman Filter** is used to maintain the identity of objects across multiple frames.
   - **Tracker Integration**: The tracker uses the object detection results to track each object over time, ensuring that IDs are consistently assigned as objects move through the frames.
* New Object Detection :
   - **New Object Detection Logic**: The algorithm checks for new objects in each frame by comparing the current set of tracked objects with the previous frame. If an object ID is not present in the previous frame, it is marked as a new object.
* Missing Object Detection :
   - **Object Tracking**: The system tracks previously seen objects and checks for their presence in the current frame. If an object’s ID is missing from the current frame, it is identified as a "missing object."
   - **Historical Tracking**: A history of tracked object IDs is maintained to detect when an object disappears or reappears.
* FPS Calculation :
   - **Performance Metrics**: The frames-per-second (FPS) is calculated for real-time performance evaluation. FPS is computed by measuring the time taken to process each frame and displaying it in the video output to evaluate how well the system performs in real-time.
* Dockerization :
   - **Containerized Environment**: The project is containerized using Docker, allowing it to run in an isolated environment with all the necessary dependencies. This ensures consistency across different systems and simplifies deployment and testing.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Follow the <a href="#getting-started">Getting Started</a> guide
3. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
4. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


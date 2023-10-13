# SubSeaSignal- RockVsMine
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#Overview">Overview</a>
        </li>
        <li>
            <a href="#meet_the_team">Meet The Team</a>
        </li>
        <li>
            <a href="#SubSeaSignal">SubSeaSignal</a>
        </li>
        <ul>
            <li><a href="#project-overview">Project Overview</a></li>
            <li><a href="#team-members">Team Members</a></li>
            <li><a href="#instructions">Instructions</a></li>
            <li><a href="#conclusion">Conclusion</a></li>
            <li><a href="#data-source">Data Source</a></li>
            <li><a href="#acknowledgments">Acknowledgement</a></li>
        </ul>
    </ol>
</details >

<h2 id="Overview">
 <img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width="25" class="overviews"><b> Overview</b>
</h2>
This is the project repository for a project called "SubSeaSignal" in which we have basically performed rock and mine classification.This project would make underwater travels even more safer, and this technology could be improved further to even be used in practical use cases:)
We have used data science technologies to make this project and also created a wonderful website for it to publicaly avail it, anyone having access to internet can use it.
Our project just requires you to input dimensions of the object and it would easily classify it as a rock or a mine. It can be used with technologies like SONAR with some slight modifications.

Video presentation available - <a href="https://youtu.be/xnO65jDGpDU?si=WeiCQov4fMLiQXTX">here</a>

Python Notebook available - <a href="https://github.com/VAMSIKRISHNA2210/Rocks-vs-Mines/blob/main/Mines_vs_Rocks_data_exploration_%20(1).ipynb">here</a>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<h2 id="meet_the_team">
<img src="https://media.giphy.com/media/W5eoZHPpUx9sapR0eu/giphy.gif" width="30px" alt="Git"/>&nbsp;<b>Meet The Team</b>
 </h2>

<ul>
    <li>
        <strong>Frontend/Backend dev/ML engineer:</strong> Shibam Roy - I am Shibam roy, a 16 year old school student with knowledge of Python, C++ , Data science , basic DSA and Web development.I am a Data science and tech enthusiast.I want to change the world with tech:)
    </li>
    <br>
    <li>
        <strong>Data Engineer:</strong> Vamsi Krishna Reddy - I am Vamsi Krishna, I am a 3rd-year B.tech student from SRM, Chennai. I am a machine learning and Artificial Intelligence Enthusiast. I like to make a twist on the traditional algorithm techniques to make them stand out.
    </li>
    <li>
        <strong>Data Scientist :</strong> Bhavishya Reddy  - I am Bhavishya Reddy, I am a 3rd-year B.tech student from SRM, Chennai. I am a machine learning expert in the field of neural networks. I like to use my skills to make a difference in the everyday living
    </li>
   
</ul>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br>

<h1 id="SubSeaSignal">
    <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="35"><b>SubSeaSignal</b>
</h1>

<h2 id="project-overview">
    <b>Project Overview</b>
</h2>

Introducing the SubSeaSignal project for the tech optimum hackathon. Our project classifies between rocks and mines to provide even more safer underwater travel.We have used data science technologies to make this project and also created a wonderful website for it to publicaly avail it, anyone having access to internet can use it.
Our project just requires you to input dimensions of the object and it would easily classify it as a rock or a mine. It can be used with technologies like SONAR with some slight modifications.

<h2 id="team-members">
    <b>Team Members</b>
</h2>

- Shibam Roy: ML Engineer / Back-end developer / Front-end developer
- Vamsi Krishna Reddy: Data Engineer
- Bhavishya Reddy: Data Scientist

<h2 id="instructions">
<b>Instructions for usage </b>
</h2>

### Our overall project together:
To check our overall project altogether, you can go to our project website <a href="https://subseasignal.pythonanywhere.com/">here</a>
You can explore it and learn yourself too:)

#### Steps to Use the project:
1. Go to the project website <a href="https://subseasignal.pythonanywhere.com/">here</a>
2. Scroll to the "Test Our Project" section, and fill up your name(you may fill any name incase you dont want to share your own name)
3. Enter dimensions of the object with 60 different values, each ranging between 0-1 comma seperated.
   A test input can be:
   ``` bash
   0.02,0.0371,0.0428,0.009,....,0.0032
   ```
   In case you dont have any dimensions and yet want to check our project, you can just enter a few dimensions like 2 or 3, the rest would be autofilled by the last entered value.
4. Press the Submit button, and all done! you will be redirected to the results page:)
   
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

### Dataset Description

The dataset consists of a collection of sonar readings taken from an underwater environment. Each sonar reading is represented as a set of numerical features that capture different characteristics of the object being detected.

The dataset contains the following columns:
The dataset contains sonar readings taken from an underwater environment.

Each sonar reading is represented as a set of numerical features.

The features capture various characteristics of the object being detected by the sonar.

The dataset includes multiple feature columns, labeled as Feature_1, Feature_2, ..., Feature_n.

Each feature column contains numeric values.

The dataset also includes a target column called "Label" that indicates whether the sonar reading corresponds to a "mine" or a "rock."

The Label column contains binary values, where 0 represents a rock and 1 represents a mine.

The goal is to train a machine learning model to accurately classify new sonar readings as either mines or rocks based on their extracted features.

The dataset may require preprocessing steps such as data cleaning, feature selection, and engineering before training the model.

#### Label 
A binary label indicating whether the sonar reading corresponds to a "mine" or a "rock" (0 for rock, 1 for mine).
train a machine learning model using this dataset to accurately classify new sonar readings as either mines or rocks based on their extracted features.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<h2 id="conclusion">
<b>Conclusion</b>
</h2>
The successful development of SubSeaSignal has broad implications, especially in the context of naval operations, underwater resource exploration, and environmental monitoring. By accurately distinguishing between rocks and mines in submerged environments, SubSeaSignal enhances the safety and effectiveness of various marine activities, ultimately leading to safer navigation and reduced risks for underwater ecosystems.

The project's data-driven approach, coupled with the utilization of advanced technologies, showcases the power of data science in addressing complex and critical challenges. SubSeaSignal not only offers a practical and effective solution but also serves as a testament to the continuous advancement of data science in tackling real-world problems.

Moving forward, the SubSeaSignal project can further evolve and be fine-tuned with more extensive datasets, improved sensor technology, and enhanced machine learning models. With ongoing development, we anticipate that SubSeaSignal will continue to contribute to the advancement of marine safety and exploration, making our underwater world a safer and more accessible place for generations to come.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<h2 id="data-source">
<b>Data Source</b>
</h2>
We are thankful to all the data source through which we have accessed the data, here is the source:
<ul>
    <li><a href="https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data">SONAR Data</a></li>
</ul>

<h2 id="acknowledgements">
<b>Acknowledgements</b>
</h2>

We would like to express our sincere gratitude to Tech Optimum for organizing the hackathon that inspired this website. The hackathon was a well-organized and challenging event that provided us with the opportunity to learn new skills, collaborate with talented individuals, and develop this website.
We would also like to thank the following people for their support and guidance throughout the development of this website
Without your help and support, this website would not have been possible. Thank you!


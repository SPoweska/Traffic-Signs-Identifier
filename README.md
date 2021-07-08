# Traffic Signs Identifier

<img src="https://i.ibb.co/n6h8BT3/Logo.png" width="400">

## Table of contents

* [General Information](#general-information)
* [Technologies](#technologies)
* [Setup](#setup)
* [Model](#model)
* [Screenshots](#screenshots)
* [Contributors](#contributors)
* [Sources](#sources)
* [License](#license)

## General Information

The aim of this project was to create a web application that allows users to efficiently and quickly check the traffic sign on a selected photo. After loading the photo, the application displays the most likely signature of a traffic sign.

## Technologies
* Python - version 3.8.10
* Flask - version 2.0.1
* Flask-WTF - version 0.15.1
* TensorFlow - version 2.5.0
* Keras - version 2.4.3
* Pillow - version 8.2.0
* Matplotlib - version 3.4.2
* And more..

## Setup

To run Traffic Signs Identifier app, follow these steps:

1. Clone the repository.
2. Install required Python dependencies: 
```
pip install -r requirements.txt
```
3. Start the application
```
export FLASK_APP=app.py
flask run
```
or
```
export FLASK_APP=app.py
python -m flask run
```
or using IDE like PyCharm.

If you have trouble launching the application, please refer to the [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/).

## Model

Training Loss and Accuracy

<img src="https://i.ibb.co/6WGv4VN/plot.png">

Train your own model with this command: 
```
python model_train.py --dataset [dataset_path] --model [model_output_path/name.model] --plot [plot_output_path/name.png]
```

## Screenshots

1. Main Page
<img src="https://i.ibb.co/fD3TXdq/main-page.png" width="1000">

2. Results page
<img src="https://i.ibb.co/t2xzRqq/results-page.png" width="1000">


## Contributors

Thanks to the following people who have contributed to this project:

* [Karol Jarosz 60104](https://github.com/TheHaRyPL) 
* [Marcin Kołek 60102](https://github.com/DowelMartin) 
* [Sebastian Powęska 60068](https://github.com/SPoweska) 

## Sources

* Dataset: [Stallkamp, J., Schlipsing, M., Salmen, J. i Igel, C. (2011). The {G}erman {T}raffic {S}ign {R}ecognition {B}enchmark: A multi-class classification competition.](https://benchmark.ini.rub.de/)  

## License

This project uses the following license: [MIT](https://choosealicense.com/licenses/mit/).



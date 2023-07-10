# **Deployment**

## **Contents**

1. [GitHub/Gitpod](#githubgitpod)
   - [Create Repository](#create-repository)
   - [Setting up the Workspace](#setting-up-the-workspace)
2. [ElephantSQL Database](#elephantsql-database)
3. [AWS Setup](#aws-setup)
   - [S3 Bucket Setup](#s3-bucket-setup)
   - [IAM Group And User Setup](#iam-group-and-user-setup)
      - [Create Group](#create-group)
	  - [Create User](#create-user)
   - [Media Folder Setup](#media-folder-setup)
   - [Connecting To Workspace](#connecting-to-workspace)
4. [settings.py Media Setup](#settingspy-media-setup)  
5. [Heroku Deployment](#heroku-deployment) 
6. [Forking The Repository](#forking-the-repository)
7. [Clone The Repository](#clone-the-repository)

Below are the steps I took to deploy the site to Heroku.

## **GitHub/Gitpod**

### **Create Repository**

This project was developed by forking a custom [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.

- Click the template link above
- Click use this template and create a new respository
- Name the repository
- Launch using the Gitpod web extension

### **Setting up the Workspace**

Below were the steps taken to install the relevant packages to setup django on the workspace using the terminal.

1. Install django using - pip install django==3.2
2. Install gunicorn using - pip install gunicorn
3. Install dj_database_url using - pip install dj_database_url
4. Install psycopg using - pip install psycopg2-binary
5. Create requirements.txt file and freeze installed packages into file using - pip freeze --local > requirements.txt
6. Create django project using - django-admin startproject "your-project-name"
7. Create the first app within the project using - python manage.py startapp "your-app-name"
8. Add the created app to installed apps in the settings.py file
9. Make migrations using - python manage.py makemigrations
10. Migrate the changes using - python manage.py migrate
11. Open up the server to make sure your django project was created successfully using - python manage.py runserver 
  - If the project was created succesfully you will see the django success page.
12. Create env.py file to secure variables you dont want pushed to github.
13. In env.py file create 2 variables
```shell
   - 1. os.environ["SECRET_KEY"] = "any-secret-key-you-want"
   - 2. os.environ["DEVELOPMENT"] = "True"
```   
14. Change SECRET_KEY variable in settings.py to - SECRET_KEY = os.environ.get('SECRET_KEY')
15. Change Debug variable in settings.py to -  DEBUG = "DEVELOPMENT" in os.environ
  - With this change debug will be set to True in development and False in production.

[Top of page &uarr;](#contents)  

## **ElephantSQL Database**

This project uses ElephantSQL for the PostgreSQL Database.

The following steps were followed to setup the database and link it to the project.

1. Sign up for a new ElephantSQL account and login.
2. From the dashboard click "create new instance".
3. Name your instance. It is best practice to name the instance the same as your created django project.
4. Select the Tiny Turtle (Free) plan.
5. Select the region that is the closest to your location.
6. Navigate back to the dashboard and click on your created instance.
7. Copy the url to your clipboard.
8. Back in your workspace create a new variable in your env.py file and assign it to the copied url -
```shell
 os.environ["DATABASE_URL"] = "postgres://your-database-url"
```
9. In settings.py change the database variable to your postgres database using an if else block - 
```shell
if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```
10. Migrate the project files to your database using - python manage.py migrate.
11. On the ElephantSQL dashboard navigate to explorer and ensure your project files are there.    

[Top of page &uarr;](#contents)

## **AWS Setup**

 This project uses [AWS](https://aws.amazon.com) s3 bucket to serve static files.

The following steps were followed to setup the bucket and connect it to the project.

### **S3 Bucket Setup**

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click Save.
- From the **Permissions** tab, paste in the following CORS configuration:

  ```shell
  [
  	{
  		"AllowedHeaders": [
  			"Authorization"
  		],
  		"AllowedMethods": [
  			"GET"
  		],
  		"AllowedOrigins": [
  			"*"
  		],
  		"ExposeHeaders": []
  	}
  ]
  ```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
- Policy Type: **S3 Bucket Policy**
- Effect: **Allow**
- Principal: `*`
- Actions: **GetObject**
- Amazon Resource Name (ARN): **paste-your-ARN-here**
- Click **Add Statement**
- Click **Generate Policy**
- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

  ```shell
  {
  	"Id": "Policy1234567890",
  	"Version": "2012-10-17",
  	"Statement": [
  		{
  			"Sid": "Stmt1234567890",
  			"Action": [
  				"s3:GetObject"
  			],
  			"Effect": "Allow",
  			"Resource": "arn:aws:s3:::your-bucket-name/*"
  			"Principal": "*",
  		}
  	]
  }
  ```

- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
- Click **Save**.

- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

[Top of page &uarr;](#contents)

### **IAM Group and User setup**

The next steps in setting up the bucket is creating an IAM group and user to give bucket permissions. The IAM group and user was set up following these steps.

#### **Create Group**

- Navigate back to the aws dashboard and search for IAM.
- From user groups select "create new group"
- Select a name for your group. It is best practise t name your group similiarly to your project.
- From the user groups section click on your newly created group and navigate to the permissions tab.
- Open the add permissions dropdown and click attach policies
- Select the policy, then click add Permissions at the bottom when finished.
- From the JSON tab, select the Import Managed Policy link.
- Search for S3, select the AmazonS3FullAccess policy, and then Import.
- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.
```shell
  {
  	"Version": "2012-10-17",
  	"Statement": [
  		{
  			"Effect": "Allow",
  			"Action": "s3:*",
  			"Resource": [
  				"arn:aws:s3:::your-bucket-name",
  				"arn:aws:s3:::your-bucket-name/*"
  			]
  		}
  	]
  }
  ```

- Click Review Policy.
- Name your policy. It is best practise to name your policy the same as your group. "yourgroup-policy"
- Enter a poicy description
- Click Create Policy.  
- From User Groups, select your created group.
- Click Attach Policy.
- Search for the policy you've just created, select it, then click Attach Policy.

[Top of page &uarr;](#contents)

#### **Create User**

- From User Groups, click Add User.
- Name your user. It is best practice to name the user with the group name attached. "yourgroup-user".
- For Select AWS Access Type, select Programmatic Access.
- Add your user to to your created group.
- Click Create User.

- Once the user is created a "download csv" link will appear.
- Click it to download your users secret keys to your machine.
  - Once you pass this page there will be no option to download the file without generating new keys so ensure you download the file.
- The file will contain 2 keys which you will need to connect the user to your workspace and heroku.
   - `AWS_ACCESS_KEY_ID` = **Access key ID**
   - `AWS_SECRET_ACCESS_KEY` = **Secret access key**  

### **Media Folder Setup**

- From the s3 dashboard navigate to your created bucket
- Create a new folder called "media"
- From Manage Public Permissions select Grant public read access to this object(s)
- Upload all of the media images from your project to the bucket by clicking the upload button inside the media folder.

### **Connecting to workspace**

These steps were followed to connect the created s3 bucket to the workspace.

- Install boto3 using - pip install boto3
- Install django storages using - pip install django-storages
- freeze packages to requirements.txt using - pip freeze --local>requirements.txt
- Add storages to installed apps in settings.py
- In env.py add the user keys downloaded from the csv file
   ```shell
  os.environ["AWS_ACCESS_KEY_ID"] = "your_aws_accesskeyid"
  os.environ["AWS_SECRET_ACCESS_KEY"] = "your_aws_secretkey"
  ```

[Top of page &uarr;](#contents)  

## **settings.py Media setup**

To link the s3 bucket to your project add the following variables in settings.py

 ```shell
     if "USE_AWS" in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = "pc-haven"
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Static and media files
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"

    # Override static and media URLs in production
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
  ```

- Create a file call "Custom_storages.py" in the main directory of the project and add the following code:

  ```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
  	location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
  	location = settings.MEDIAFILES_LOCATION
  ```

- Once this code is added your bucket will be connected to your project.

[Top of page &uarr;](#contents)

## **Heroku Deployment**

The following steps were followed to deploy the project on Heroku.


- Go to [Heroku](https://dashboard.heroku.com/apps) and click "New" to create a new app.
- After choosing the app name and setting the region, press "Create app".
- Go to "Settings" and navigate to Config Vars, enter the below

    | Key                     | Value                                                                  |
    | ----------------------- | ---------------------------------------------------------------------- |
    | `DATABASE_URL`          | insert your own ElephantSQL database URL here                          |
    | `SECRET_KEY`            | insert your Django secret key                                          |
    | `DISABLE_COLLECTSTATIC` | 1 (_this is temporary and can be removed when static files available_) |
    | `PORT`                  | 8000                                                                   |
    | `AWS_ACCESS_KEY_ID`     | insert your own AWS Access Key ID key here                             |
    | `AWS_SECRET_ACCESS_KEY` | insert your own AWS Secret Access key here                             |
    | `USE_AWS`               | True                                                                   |

- Leave "Settings" and go to "Deploy". Scroll down and set Deployment Method to GitHub.
   Once GitHub is chosen, find your repository and connect it to Heroku.
- Scroll down to Manual Deploy, make sure the "main" branch is selected, and click "Deploy Branch".

[Top of page &uarr;](#contents)

## **Forking The Repository**

**To Fork the repository follow these steps:**

1. Go to [Github](https://github.com/) from your browser.
2. Navigate to the repository named [Burgers-R-Us-P5](https://github.com/seanj06/Burgers-R-Us-P5)
3. Locate the "fork" button at the top right of the page
4. Change the name and add a description of the forked repository if you wish to
5. Click Create Fork.
6. You should now have a forked version of the repository.

[Top of page &uarr;](#contents)

## **Clone The Repository**

**To Clone the repository follow these steps**

1. Go to [Github](https://github.com/) from your browser.
2. Navigate to the repository named [Burgers-R-Us-P5](https://github.com/seanj06/Burgers-R-Us-P5)
3. Click on the arrow on the green "Code" button at the top of the page.
4. Copy the HTTPS url to your clipboard.
5. In the terminal in your code editor change the directory to the location you want to clone the repository to.
6. Type "git clone" into the terminal followed by the HTTPS url you copied to your clipboard.
7. Press enter, your cloned repository should be created in the directory you specified.

[Top of page &uarr;](#contents)


























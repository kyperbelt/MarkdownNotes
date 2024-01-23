# First Week Setup using Linux

## Installing Java JDK version 17

The installation guide suggests to use the Oracle website jdk, but I went ahead and installed the [amazon correto version](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/downloads-list.html). 

## Installing JOGL 

Went to the [jogamp.com](https://jogamp.org) website as specified in the install instructions and downloaded `jogamp-fat.jar` version 2.50 from the **Builds/Downloads** section of the home page.

I placed this jar in a folder in my home directory called `java_graphics_libraries`. So the full path is `~/java_graphics_libraries/jogamp-fat.jar`.

<div class="warning">
Note that we have just put it into a folder and this does not yet count as an installation in the traditional sense. I still have to do additional work to get it to run.
</div>

## Installing JOML
Went ahead and got the JOML jar from the [releases](https://github.com/JOML-CI/JOML/releases) page of their github and put it in the same folder as the JOGL jar.

## Setting up Pathing
This will be done by editing and sourcing my `.bashrc` file. 

I dont want to create a `CLASSPATH` in my configuration, so instead i created a`JAVA_GRAPHICS_GAMING_LIBGS` environment variable which is a path where both these library jars are located.

```sh 
export JAVA_GRAPHICS_GAMING_LIBS="$HOME/java_graphics_libraries"
```
In this case `$HOME` just expands to my home folder `/home/kyperbelt/`. 

## Downloading and Running Tumpling Cube Example

I downloaded the tumbling cube example and opened it up. Since I am using Linux I am unable to make use of the batch files that come included. What I had to do was create new shell scripts. 

#### `compile.sh`
```sh 
javac -cp $JAVA_GRAPHICS_GAMING_LIBS/*:. code/Code.java
```

#### `run.sh`
```sh 
java -cp $JAVA_GRAPHICS_GAMING_LIBS/*:. --add-exports java.base/java.lang=ALL-UNNAMED --add-exports java.desktop/sun.awt=ALL-UNNAMED --add-exports java.desktop/sun.java2d=ALL-UNNAMED -Dsun.java2d.d3d=false -Dsun.java2d.uiScale=1 code.Code
```
I have to specify the `-cp (classpath)` option in my scripts because I did not define the `CLASSPATH` environment variable. We could have defined it locally, but I chose to just inline it. 

#### Here is the result 
![](../assets/tumplecube.gif)

## Code Completion and IDE help!

Because I am using nvim, having the above rudementary setup was pretty nightmarish. I was unable to get any kind of code completion or lsp diagnostics, but I was able to fix this with a few simple steps. 

1. #### Init Gradle 
    I ran `gradle init` and selected the `Basic` option from the drop down. This creates a barebones **build.gradle** file which I can use to get the **JDT** Language server to work with.  
2. ####  Restructure
    I created a new `src` directory in the Tumbling Cube example folder, and then I dragged in the `code`directory and all the contents into it so the structure looked like this: 
    ```text 
    TumblingCube/
    └-src/
       ├-compile.sh 
       ├-compile.bat 
       ├-run.sh 
       ├-run.bat 
       └-code/ 
           ├-Code.java
           ├-Utils.java
           └-<otherfiles>
    ```

    Then in my **build.gradle** I put the following: 
    ```java
    plugins{
            id 'application'
    }

    dependencies {
            // import local jars from environment variable
            implementation fileTree(dir: System.getenv('JAVA_GRAPHICS_GAMING_LIBS'), include: ['*.jar'])
    }
    
    sourceSets{
            main{
                    java{
                            srcDirs = ['src']
                    }
                    resources{
                            srcDirs = ['src']
                    }
            }
    }

    tasks.named('run').configure {
        workingDir =file('src') 
    }

    jar {
    manifest {
        attributes(
            'Main-Class': 'code.Code'
        )
    }

    from {
            configurations.runtimeClasspath.collect { it.isDirectory() ? it : zipTree(it) }
    }
    }

    application {
            mainClass = 'code.Code'
    }
    ```
    This added a bunch of tasks to the gradle because of the `application` plugin and it lets me use `./gradlew run` to run the application, but most importantly it allows jdtls to pick up my project, index it, and give me that sweet, sweet IDE experience!

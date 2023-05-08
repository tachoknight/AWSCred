# AWSCred
This is a small script I wrote for fun to help me manage my various AWS accounts. It can list the credentials in your ~/.aws/credentials file, and it can also switch between them. 

It modifies the `$HOME/.aws/credentials` file directly, so it's not a good idea to run it while you have other programs that are using the credentials file.

## Installation
The script is written in Python 3 so you'll that installed. I put the script in my `$HOME/bin` directory, but you can put it wherever you want. Just make sure that directory is in your `$PATH`.

## Usage
``` awscred``` - Lists the credentials in your credentials file

``` awscred <profile>``` - Switches to the specified profile



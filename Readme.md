# Malclean
### Description
Malclean is a Python script for removing harmful code from files. This script was created with the assumption that bulk malware injections typically occur at the beginning or end of a file. As a result, the script focuses on harmful code that fits this scenario.

### Usage

###### Before using this script, make sure to change the python binary file path within the shebang.
There are two modes that you can run this script with. **Dry_Run** & **Live_Run**
##### Dry_Run Mode
To run this script in dry_run mode, toggle the parameter **--dry-run**. The dry-run mode ensures that any modifications made by the script do not affect the live file. In this mode, the script displays the file's appearance after cleanup.

##### Live_Run Mode
This is the mode in which the modifications are applied to the original file. If the --dry-run argument is not provided, the script will default to executing in live_run mode.

#### Parameters
The script takes three **must-use** parameters and one optional parameter.

**-f**  **-** Specify the file that needs to be cleaned up.
**-b** **-** Specify the begin pattern of the malicious code.
**-e** **-** Specify the end pattern of the malicious code.

**Optional**
**--dry-run** **-** Execute the script in dry-run mode.

#### Syntax
````
./malclean.py -f </path/to/malicious/file> -b "start of malicious code" -e "end of malicious code" --dry-run
./malclean.py -f </path/to/malicious/file> -b "start of malicious code" -e "end of malicious code"
````

#### Example
**Dry_Run**
````
$ cat maltext.txt 
asdkjpjdkadfj]dsfjqrqow[idndnpqkjfdpoqwjksdfnvkdfjqkpwrjpoqwfjdwnfkdfdfsdfsdfadqwdqwd
;if(ndsw===undefined) klpdjfpajfpsdfpwdfjdpsgfskpgjeq[orp[0wo[dgjpsgjwefdfjlpsfgj[osg[qer]qorwpgkl;fmsf;lgmwepkrotopwrjgipowrjgiwrjgirwtji2rjtirjtmitjmitj
wdgfoiwrgwpjtpweqtjrwpejrwpoerjweporfjgnwortjipwejtriwepojtripowetjrwrptjwirt
());};

$ ./malclean_args1.py -f maltext.txt -b ";if(ndsw===undefined)" -e "());};" --dry-run
asdkjpjdkadfj]dsfjqrqow[idndnpqkjfdpoqwjksdfnvkdfjqkpwrjpoqwfjdwnfkdfdfsdfsdfadqwdqwd

$ cat maltext.txt 
asdkjpjdkadfj]dsfjqrqow[idndnpqkjfdpoqwjksdfnvkdfjqkpwrjpoqwfjdwnfkdfdfsdfsdfadqwdqwd
;if(ndsw===undefined) klpdjfpajfpsdfpwdfjdpsgfskpgjeq[orp[0wo[dgjpsgjwefdfjlpsfgj[osg[qer]qorwpgkl;fmsf;lgmwepkrotopwrjgipowrjgiwrjgirwtji2rjtirjtmitjmitj
wdgfoiwrgwpjtpweqtjrwpejrwpoerjweporfjgnwortjipwejtriwepojtripowetjrwrptjwirt
());};
````

**Live_Run**
````
$ cat maltext.txt 
asdkjpjdkadfj]dsfjqrqow[idndnpqkjfdpoqwjksdfnvkdfjqkpwrjpoqwfjdwnfkdfdfsdfsdfadqwdqwd
;if(ndsw===undefined) klpdjfpajfpsdfpwdfjdpsgfskpgjeq[orp[0wo[dgjpsgjwefdfjlpsfgj[osg[qer]qorwpgkl;fmsf;lgmwepkrotopwrjgipowrjgiwrjgirwtji2rjtirjtmitjmitj
wdgfoiwrgwpjtpweqtjrwpejrwpoerjweporfjgnwortjipwejtriwepojtripowetjrwrptjwirt
());};

$ ./malclean_args1.py -f maltext.txt -b ";if(ndsw===undefined)" -e "());};"

$ cat maltext.txt 
asdkjpjdkadfj]dsfjqrqow[idndnpqkjfdpoqwjksdfnvkdfjqkpwrjpoqwfjdwnfkdfdfsdfsdfadqwdqwd
````
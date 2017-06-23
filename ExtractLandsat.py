''' 

#### Florian Beyers script to extract Landsat-Data vom *.tar.gz in a folder
### with Python 2.7
## 2017-05-24
# mail@flobeyer.de

   Copyright 2015 Florian Beyer
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
   
       http://www.apache.org/licenses/LICENSE-2.0
       
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 '''


# import packages
import tarfile
from os import listdir, makedirs
from os.path import isfile, join, exists

# directory where the Lansat data are stored
load_path = "C:/path/path/"

# the folder where the data shall be extracted to
save_folder = 'extracted/'


if not exists(join(load_path,save_folder)):
    # testing the existence of the Extraction Folder
    makedirs(join(load_path, save_folder))
# creating output directory
save_path = join(load_path, save_folder)

# reading all files in the loading path
onlyfiles = [f for f in listdir(load_path) if isfile(join(load_path, f))]
del(f)

# extract the *.tar.gz files from onlyfiles
onlytars = []
for filenames in onlyfiles:
    if filenames[-7:] == '.tar.gz':
        onlytars.append(filenames)
del(onlyfiles) # onlyfiles is not necessary anymore

# final loop to extract the data and store them to the save_path
i = 1
for filenames in onlytars:
    ## read one file as pandas dataframe
    temp = tarfile.open(join(load_path, filenames))
    if not exists(join(save_path, filenames)):
        makedirs(join(save_path, filenames[:-6]))
    temp.extractall(join(save_path, filenames[:-6]))
    temp.close()
    print '{} from {} extracted'.format(i,len(onlytars))
    i +=1

# deleting all remaining variables 
del(i, temp, filenames, onlytars, load_path, save_path, save_folder)   

print 'Extraction successfull'

# Project
'Natural Language Processing for Hindi from hinglish to hindi Devanagari'
The roman script and devanagari script dataset is used to train the model to tansliterate hindi from roman to devanagari script


We have used dataset from Dakshina Dataset from google apis which contains mapping between hindi in roman and same in devanaagri script
First we separate the words and then the words into characters for each script. These characters are kept with index in the arrays.
We then have created the matrix in three dimensional arrays to store the values in one hot format and then we used the same values to train the model.
Then we use the test data to check on the model.
We create the LSTM model.
The accuracy of the model is around 97 percent

We check for conversion from Roman script to devanagri and devanagri to roman using reverse tokens and tokens.


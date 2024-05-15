# Overview of the new neural network system in Tesseract 4.00


## Introduction
The neural network system in Tesseract pre-dates Tensor Flow, but is compatible with it, as there is a network description language called [Variable Graph Specification Language (VGSL)](https://github.com/tesseract-ocr/tesseract/wiki/VGSLSpecs), that is also available for Tensor Flow. [See] (https://github.com/tensorflow/models/tree/master/street)


## Integration with Tesseract
The neural network engine is selected by specifying OEM_LSTM_ONLY as the OcrEngineMode to TessBaseAPI::Init. (It will probably be made the default by release of 4.00.) From an API perspective, that is all that is required to use it. To recognize text from an image of a single text line, use SetPageSegMode(PSM_RAW_LINE). This can be used from the command-line with -psm 13
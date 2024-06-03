from torchvision.io.image import read_image
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights
from torchvision.models.segmentation import lraspp_mobilenet_v3_large, LRASPP_MobileNet_V3_Large_Weights
from torchvision.transforms.functional import to_pil_image

# img = read_image("gallery/assets/dog1.jpg")
img_path = 'd:\\pic\\dog1.jpg'
img = read_image(img_path)

# Step 1: Initialize model with the best available weights
'''
weights = FCN_ResNet50_Weights.DEFAULT
model = fcn_resnet50(weights=weights)
'''
weights = LRASPP_MobileNet_V3_Large_Weights.DEFAULT
print(weights)
print(weights.meta['categories'])
model = lraspp_mobilenet_v3_large(weights=weights)
model.eval()

# Step 2: Initialize the inference transforms
preprocess = weights.transforms()

# Step 3: Apply inference preprocessing transforms
batch = preprocess(img).unsqueeze(0)

# Step 4: Use the model and visualize the prediction
prediction = model(batch)["out"]
print(type(prediction), prediction.shape)
normalized_masks = prediction.softmax(dim=1)
print(type(normalized_masks), normalized_masks.shape)

class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta["categories"])}
mask = normalized_masks[0, class_to_idx["dog"]]
print(type(mask), mask.shape)
to_pil_image(mask).show()

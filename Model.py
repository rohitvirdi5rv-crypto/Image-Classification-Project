import pathlib
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential, save_model

dataset_url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'

data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)

data_dir = pathlib.Path(data_dir) / 'flower_photos'

image_count = len(list(data_dir.glob('*/*.jpg')))
print('Total number of images: ', image_count)

batch_size = 32
image_height = 180
image_width  =180

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "training",
    seed = 123,
    image_size=(image_height,image_width),
    batch_size=batch_size
)

val_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "validation",
    seed = 123,
    image_size = (image_height,image_width),
    batch_size = batch_size
)

class_names = train_dataset.class_names
print("class names:", class_names)

train_dataset = train_dataset.cache().shuffle(1000)
val_dataset = val_dataset.cache()

num_classes = len(class_names)
print('num classes:', num_classes)

model = Sequential([
    layers.Rescaling(1./255, input_shape=(image_height, image_width,3)),
    layers.Conv2D(16,3, padding ='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32,3, padding = 'same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64,3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation = 'relu'),
    layers.Dense(num_classes)
])

model.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, reduction = 'sum_over_batch_size'),
    metrics = ['accuracy']
)

model.summary()

## Model Training
epochs = 20
history = model.fit(
    train_dataset,
    validation_data = val_dataset,
    epochs = epochs
)

save_model(model, 'Image_Classification_Model.hdf5')
print('model saved')
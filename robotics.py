{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "501ebc3d-60b6-41b4-a274-e410a82ab9f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found 240 images belonging to 2 classes.\n",
      "Found 60 images belonging to 2 classes.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\anaconda\\Lib\\site-packages\\keras\\src\\layers\\convolutional\\base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.\n",
      "  super().__init__(activity_regularizer=activity_regularizer, **kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 436ms/step - accuracy: 0.4833 - loss: 0.7229 - val_accuracy: 0.5000 - val_loss: 0.7119\n",
      "Epoch 2/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 159ms/step - accuracy: 0.6292 - loss: 0.6319 - val_accuracy: 0.4833 - val_loss: 0.7240\n",
      "Epoch 3/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 152ms/step - accuracy: 0.7625 - loss: 0.5330 - val_accuracy: 0.5167 - val_loss: 1.1184\n",
      "Epoch 4/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 160ms/step - accuracy: 0.7458 - loss: 0.5186 - val_accuracy: 0.6833 - val_loss: 0.6909\n",
      "Epoch 5/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 147ms/step - accuracy: 0.8208 - loss: 0.4405 - val_accuracy: 0.5833 - val_loss: 0.7177\n",
      "Epoch 6/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m3s\u001b[0m 157ms/step - accuracy: 0.7875 - loss: 0.4468 - val_accuracy: 0.5333 - val_loss: 1.1440\n",
      "Epoch 7/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 157ms/step - accuracy: 0.8042 - loss: 0.4265 - val_accuracy: 0.4833 - val_loss: 0.8842\n",
      "Epoch 8/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 158ms/step - accuracy: 0.8458 - loss: 0.3668 - val_accuracy: 0.6667 - val_loss: 0.8087\n",
      "Epoch 9/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 156ms/step - accuracy: 0.8250 - loss: 0.3773 - val_accuracy: 0.5500 - val_loss: 1.4728\n",
      "Epoch 10/10\n",
      "\u001b[1m15/15\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 158ms/step - accuracy: 0.7958 - loss: 0.4043 - val_accuracy: 0.6167 - val_loss: 1.0413\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:absl:You are saving your model as an HDF5 file via `model.save()` or `keras.saving.save_model(model)`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')` or `keras.saving.save_model(model, 'my_model.keras')`. \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Training Complete!\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
    "from tensorflow.keras import layers, models\n",
    "\n",
    "# ✅ YOUR DATASET PATH\n",
    "data_dir = r\"D:\\Robotcd project\\Dataset\"\n",
    "\n",
    "img_size = 64\n",
    "batch_size = 16\n",
    "\n",
    "# 🔁 Data preprocessing\n",
    "datagen = ImageDataGenerator(\n",
    "    rescale=1./255,\n",
    "    rotation_range=20,\n",
    "    zoom_range=0.2,\n",
    "    horizontal_flip=True,\n",
    "    validation_split=0.2\n",
    ")\n",
    "\n",
    "# 📂 Training data\n",
    "train = datagen.flow_from_directory(\n",
    "    data_dir,\n",
    "    target_size=(img_size, img_size),\n",
    "    batch_size=batch_size,\n",
    "    class_mode='categorical',\n",
    "    subset='training'\n",
    ")\n",
    "\n",
    "# 📂 Validation data\n",
    "val = datagen.flow_from_directory(\n",
    "    data_dir,\n",
    "    target_size=(img_size, img_size),\n",
    "    batch_size=batch_size,\n",
    "    class_mode='categorical',\n",
    "    subset='validation'\n",
    ")\n",
    "\n",
    "# 🧠 MODEL\n",
    "model = models.Sequential([\n",
    "    layers.Conv2D(16, (3,3), activation='relu', input_shape=(64,64,3)),\n",
    "    layers.MaxPooling2D(2,2),\n",
    "\n",
    "    layers.Conv2D(32, (3,3), activation='relu'),\n",
    "    layers.MaxPooling2D(2,2),\n",
    "\n",
    "    layers.Flatten(),\n",
    "    layers.Dense(64, activation='relu'),\n",
    "    layers.Dense(2, activation='softmax')\n",
    "])\n",
    "\n",
    "# ⚙️ Compile\n",
    "model.compile(\n",
    "    optimizer='adam',\n",
    "    loss='categorical_crossentropy',\n",
    "    metrics=['accuracy']\n",
    ")\n",
    "\n",
    "# 🚀 Train\n",
    "model.fit(train, validation_data=val, epochs=10)\n",
    "\n",
    "# 💾 Save model\n",
    "model.save(\"model.h5\")\n",
    "\n",
    "print(\"✅ Training Complete!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d72dc6dc-30bd-489c-83aa-ee153b55ffa3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "INFO:tensorflow:Assets written to: C:\\Users\\patta\\AppData\\Local\\Temp\\tmplme3cz_1\\assets\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO:tensorflow:Assets written to: C:\\Users\\patta\\AppData\\Local\\Temp\\tmplme3cz_1\\assets\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved artifact at 'C:\\Users\\patta\\AppData\\Local\\Temp\\tmplme3cz_1'. The following endpoints are available:\n",
      "\n",
      "* Endpoint 'serve'\n",
      "  args_0 (POSITIONAL_ONLY): TensorSpec(shape=(None, 64, 64, 3), dtype=tf.float32, name='input_layer')\n",
      "Output Type:\n",
      "  TensorSpec(shape=(None, 2), dtype=tf.float32, name=None)\n",
      "Captures:\n",
      "  1993323457680: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  1993323457488: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  1993337718352: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  1993337722576: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  1993337718160: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  1993337722960: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  1993337722768: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  1993337723344: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "✅ Converted to model.tflite\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "\n",
    "# Load trained model\n",
    "model = tf.keras.models.load_model(\"model.h5\")\n",
    "\n",
    "# Convert to TFLite\n",
    "converter = tf.lite.TFLiteConverter.from_keras_model(model)\n",
    "\n",
    "# 🔥 IMPORTANT (for ESP32)\n",
    "converter.optimizations = [tf.lite.Optimize.DEFAULT]\n",
    "\n",
    "tflite_model = converter.convert()\n",
    "\n",
    "# Save file\n",
    "with open(\"model.tflite\", \"wb\") as f:\n",
    "    f.write(tflite_model)\n",
    "\n",
    "print(\"✅ Converted to model.tflite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9347a050-8c0d-41e1-a922-d4cb87f454b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\anaconda\\Lib\\site-packages\\keras\\src\\export\\tf2onnx_lib.py:8: FutureWarning: In the future `np.object` will be defined as the corresponding NumPy scalar.\n",
      "  if not hasattr(np, \"object\"):\n",
      "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "INFO:tensorflow:Assets written to: C:\\Users\\patta\\AppData\\Local\\Temp\\tmp3zwuejhd\\assets\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO:tensorflow:Assets written to: C:\\Users\\patta\\AppData\\Local\\Temp\\tmp3zwuejhd\\assets\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved artifact at 'C:\\Users\\patta\\AppData\\Local\\Temp\\tmp3zwuejhd'. The following endpoints are available:\n",
      "\n",
      "* Endpoint 'serve'\n",
      "  args_0 (POSITIONAL_ONLY): TensorSpec(shape=(None, 64, 64, 3), dtype=tf.float32, name='input_layer')\n",
      "Output Type:\n",
      "  TensorSpec(shape=(None, 2), dtype=tf.float32, name=None)\n",
      "Captures:\n",
      "  3019175137872: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  3019175139216: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  3019175139600: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  3019175140368: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  3019175140944: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  3019175141904: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  3019175141712: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "  3019175142288: TensorSpec(shape=(), dtype=tf.resource, name=None)\n",
      "model.tflite created\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "\n",
    "model = tf.keras.models.load_model(\"model.h5\")\n",
    "\n",
    "converter = tf.lite.TFLiteConverter.from_keras_model(model)\n",
    "converter.optimizations = [tf.lite.Optimize.DEFAULT]\n",
    "\n",
    "tflite_model = converter.convert()\n",
    "\n",
    "with open(\"model.tflite\", \"wb\") as f:\n",
    "    f.write(tflite_model)\n",
    "\n",
    "print(\"model.tflite created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f5957c53-6ae1-48b8-ac11-0a4be1b2576a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "model.h created\n"
     ]
    }
   ],
   "source": [
    "with open(\"model.tflite\", \"rb\") as f:\n",
    "    data = f.read()\n",
    "\n",
    "with open(\"model.h\", \"w\") as f:\n",
    "    f.write(\"unsigned char model_tflite[] = {\\n\")\n",
    "\n",
    "    for i, byte in enumerate(data):\n",
    "        f.write(f\"0x{byte:02x}, \")\n",
    "        if (i + 1) % 12 == 0:\n",
    "            f.write(\"\\n\")\n",
    "\n",
    "    f.write(\"\\n};\\n\")\n",
    "    f.write(f\"unsigned int model_tflite_len = {len(data)};\\n\")\n",
    "\n",
    "print(\"model.h created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2e60858-574d-45f4-bcfe-6c7d1c758395",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

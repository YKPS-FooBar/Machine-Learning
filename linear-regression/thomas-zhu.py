# I tried to reinvent the wheel.  Do NOT ever attempt that.
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalization.
area = X_train.shape[1] * X_train.shape[2]  # It's just 784.
X_train = X_train.reshape((-1, area)) / 256
X_test = X_test.reshape((-1, area)) / 256

# Make it categorical.
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# Fun part.
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(10, activation='softmax'))

early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                  patience=1)

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(X_train, y_train,
                    batch_size=512,
                    epochs=30,
                    callbacks=[early_stopping],
                    validation_split=0.1)

print(f'Test accuracy: {model.evaluate(X_test, y_test)[1] * 100:3.2f}%')

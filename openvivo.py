# from openvino import Core

# core = Core()

# print(core.available_devices)

import openvino as ov
import numpy as np
import time

# Build a simple Neural Network Graph
input_node = ov.opset13.parameter([1, 1024], np.float32)
weights = ov.opset13.constant(
    np.random.rand(1024, 1024).astype(np.float32)
)

output = ov.opset13.matmul(input_node, weights, False, False)
model = ov.Model([output], [input_node])

core = ov.Core()

print("Available devices:", core.available_devices)
print("Compiling model for NPU...")

compiled_model = core.compile_model(model, "NPU")

print("NPU is ready!")
print("Running continuously for 30 seconds...")

data = np.random.rand(1, 1024).astype(np.float32)

end_time = time.time() + 30

count = 0

while time.time() < end_time:
    compiled_model([data])
    count += 1

print("Finished!")
print("Inference count: ", count)
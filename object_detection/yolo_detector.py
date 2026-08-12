
def detect_objects(model, image_path, confidence_threshold=0.5):

    results = model(image_path)
    boxes = results[0].boxes

    image_width = results[0].orig_shape[1]

    detections = []

    for cls, conf, box in zip(boxes.cls, boxes.conf, boxes.xyxy):

        confidence = float(conf)

        if confidence < confidence_threshold:
            continue

        class_id = int(cls)
        object_name = model.names[class_id]

        x1, y1, x2, y2 = box.tolist()

        center_x = (x1 + x2) / 2

        if center_x < image_width / 3:
            position = "left"
        elif center_x < 2 * image_width / 3:
            position = "center"
        else:
            position = "right"

        detections.append({
            "name": object_name,
            "confidence": round(confidence, 3),
            "position": position,
            "bbox": [
                round(x1, 2),
                round(y1, 2),
                round(x2, 2),
                round(y2, 2)
            ]
        })

    return detections

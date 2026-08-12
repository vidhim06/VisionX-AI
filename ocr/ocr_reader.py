
def read_text(reader, image, confidence_threshold=0.5):

    results = reader.readtext(image)

    texts = []

    for bbox, text, confidence in results:

        confidence = float(confidence)

        if confidence < confidence_threshold:
            continue

        texts.append({
            "text": text,
            "confidence": round(confidence, 3),
            "bbox": bbox
        })

    return texts

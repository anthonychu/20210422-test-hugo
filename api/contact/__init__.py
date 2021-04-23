import json
import azure.functions as func


def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    text = "{name}\n{email}\n{message}"
    message.set(json.dumps({
        "content": [{
            "type": "text/plain",
            "value": text.format(**req.form)
        }]
    }))

    return func.HttpResponse(status_code=302, headers={ "location": "/contact"})

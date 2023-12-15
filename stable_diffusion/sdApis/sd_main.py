import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

def txt2img(prompt, model="stabilityai/stable-diffusion-2-1"):

    model_id = model

    # Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

    prompt = prompt
    image = pipe(prompt).images[0]
    img_path = "../media/response.png"    
    image.save(img_path)

    return img_path


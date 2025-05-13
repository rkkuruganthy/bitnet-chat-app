# bitnet_runner.py
import subprocess
import os

MODEL_PATH = "/Users/ravikuruganthy/myApps/bitnet-chat-app/models/BitNet/bitnet_b1_58-3b-q8_0.gguf"
LLAMA_CLI = "/Users/ravikuruganthy/myApps/bitnet-chat-app/llama.cpp/build/bin/llama-cli"

def run_bitnet(prompt: str, max_tokens=200) -> str:
    if not os.path.exists(MODEL_PATH):
        return f"[Error] Model not found at path: {MODEL_PATH}"

    try:
        result = subprocess.run(
            [LLAMA_CLI, "-m", MODEL_PATH, "-p", prompt, "-n", str(max_tokens)],
            capture_output=True, text=True, timeout=90
        )

        print("==== STDOUT ====")
        print(result.stdout)
        print("==== STDERR ====")
        print(result.stderr)

        if result.returncode != 0:
            return f"[Error] Return code {result.returncode}:\n{result.stderr}"

        output_lines = result.stdout.splitlines()
        response_lines = [line for line in output_lines if not line.startswith("main:")]
        return "\n".join(response_lines).strip()

    except Exception as e:
        return f"[Exception] {e}"

# 1. Large Language Models (LLMs)

An **LLM** is a neural network trained to predict the next token in text. Examples include models like Llama 3 and Qwen3.

They are good at:

- reasoning in natural language
    
- extracting structure from text
    
- deciding actions
    

But they have limitations:

- **hallucinations** (making up facts)
    
- **no direct access to real systems**
    
- **stateless by default**
    

So when you build an AI system around them, you usually combine them with **tools and external state**.

---

# 2. Tool Use (Function Calling)

Tool use is the mechanism that allows an LLM to **interact with external systems**.

Instead of directly answering a question, the model can **request a tool to run**.

Example tools in your project:

```
list_files(path)
read_file(path)
move_file(src, dst)
create_folder(path)
```

The flow looks like this:

```
User → LLM → tool call → tool executes → result → LLM
```

Example:

User asks:

```
show files in workspace
```

The model decides:

```
call list_files("./workspace")
```

The tool runs and returns the real data.

This prevents hallucination because the model **does not guess the filesystem state**.

---

# 3. Agents

An **agent** is a system where the LLM:

1. reasons about a problem
    
2. chooses actions (tools)
    
3. observes results
    
4. repeats until the task is complete
    

This is called an **agent loop**.

Example task:

```
organize my notes
```

The agent may do:

```
1. list_files
2. categorize files
3. create folders
4. move files
```

Each step involves reasoning and execution.

This loop is the key concept behind:

- autonomous AI tools
    
- AI coding assistants
    
- AI automation systems
    

---

# 4. Prompt Engineering

The **prompt** tells the model how it should behave.

Example system prompt:

```
You are an AI terminal.
Always use tools to access the filesystem.
Never guess file information.
```

Prompts define:

- the **role** of the model
    
- the **rules** it must follow
    
- the **tools available**
    

Poor prompts lead to:

- hallucinated tool calls
    
- incorrect actions
    
- random outputs
    

---

# 5. Tool Schema

Tools must be described to the model in a structured format.

Example:

```json
{
 "name": "read_file",
 "description": "Read the contents of a file",
 "parameters": {
   "type": "object",
   "properties": {
     "path": { "type": "string" }
   }
 }
}
```

This schema allows the model to understand:

- what the tool does
    
- what inputs it needs
    
- how to call it
    

Internally the model treats this like a **structured API**.

---

# 6. Sandboxing

An AI agent that interacts with a system must be **restricted**.

Otherwise it could execute dangerous operations.

Example restriction:

```
workspace/
```

All tools enforce:

```
path must start with workspace
```

This prevents the model from accessing:

```
/etc/
/Users/
/home/
```

Sandboxing is critical in:

- AI terminals
    
- autonomous agents
    
- coding assistants
    

---

# 7. Separation of Concerns (Architecture)

Well-designed AI systems separate responsibilities into layers.

Typical architecture:

```
API layer
Agent controller
LLM interface
Tool runtime
Workspace
```

Each layer has a clear role.

Example:

API layer

```
handles HTTP requests
```

Agent layer

```
controls reasoning loop
```

Tool layer

```
executes real actions
```

This modularity makes the system easier to scale and debug.

---

# 8. Deterministic Execution vs Probabilistic Reasoning

A key principle in AI system design:

```
LLM = reasoning
Code = execution
```

The LLM decides **what to do**.

The program performs **the actual action**.

Example:

LLM decides:

```
read_file("notes.md")
```

The Python code actually reads the file.

This ensures:

- correctness
    
- safety
    
- reproducibility
    

---

# 9. Context Windows

LLMs operate within a **context window**.

This is the maximum amount of text they can process at once.

Context includes:

```
system prompt
user prompt
previous messages
tool outputs
```

If the context becomes too large:

- the model forgets earlier steps
    
- performance drops
    

Agent systems must manage context carefully.

---

# 10. State Management

Most LLM APIs are **stateless**.

That means each request does not remember previous ones.

Agents maintain state manually through message history:

```
messages = [
  system prompt,
  user message,
  tool output,
  next message
]
```

This allows the model to reason across multiple steps.

---

# 11. Planning vs Execution

More advanced systems separate planning from execution.

Planner:

```
breaks task into steps
```

Executor:

```
runs each step with tools
```

Example:

Task:

```
organize workspace
```

Plan:

```
1 list files
2 group by category
3 create folders
4 move files
```

Execution:

```
run tools step by step
```

This improves reliability.

---

# 12. Model Capability

Different models have different abilities.

Small models (3B):

- faster
    
- cheaper
    
- weaker reasoning
    

Larger models (8B–14B):

- better reasoning
    
- better tool usage
    
- slower
    

For agent systems, reasoning ability matters a lot.

---

# 13. Observability

AI systems must log and inspect behavior.

Important logs:

```
model prompt
model output
tool calls
tool results
```

Without logs it is impossible to debug agent behavior.

---

# 14. Failure Handling

Agents can fail in many ways:

- hallucinated tool calls
    
- invalid arguments
    
- tool errors
    
- infinite loops
    

Systems need safeguards:

```
max steps
timeout
error recovery
```

---

# 15. Autonomous Systems

When these concepts combine, you get **autonomous agents**.

Capabilities include:

- task planning
    
- tool execution
    
- environment interaction
    
- iterative reasoning
    

Examples of systems using this pattern:

- autonomous coding assistants
    
- AI terminals
    
- workflow automation tools
    

---
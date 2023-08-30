---
title: Programming language Ideas
author: Jonathan Camarena
---
# Programming language Ideas

## Introduction

## Syntax
C-style language

### Variables
variables are mutable by default
- Variable 
    **explicit** 
    ```cpp
    var varName : type = value;
    ```
    **implicit** 
    ```cpp
    var varName := value;
    ```
- Constant
    **explicit** 
    ```cpp
    const varName : type = value;
    ```
    **implicit** 
    ```cpp
    const varName := value;
    ```
### Functions
- Rust Type (preferred) 
    ```cpp
    fn func_name(arg: type, arg2 : type) -> returnType {
        // body
    }
    ```
- Rust but return type before
    ```cpp 
    fn returnType func_name(arg: type, arg2, type) {
        // body
    }
    ```
- Arg types are before arg name
    ```cpp
    fn func_name(type arg, type arg2) -> returnType {
        // body
    }
    ```

### Error Handling
Taking Rusts Result Type but with named Errors. 
**Error func** 
```cpp
fn func_name() -> Result(type) {
   return ErrorType(error message); 
}
```
**Ok func**
```cpp
fn func_name() -> Result(type) {
   return someValue;// no need to wrap with Ok 
}
```
Propegating errors
```cpp
fn func_name() -> Result(type){
    other_func()?; // will return error if error. 

    var variable = var_func()?; // will set the value if result is not error

    // handle Result with pattern matching
    if var_func() is Ok(value) {
        variable = value;
    }

    return value_of_type; // no need to wrap in Ok. If its the correct type return will handle
}

```







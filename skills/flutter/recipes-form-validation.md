# Recipe: Form Validation and Submission

Use this when building a form with input validation, async submission, and user-safe errors.

## When to load

- You are building a form screen.
- You need a consistent validation + submit pattern.

## When NOT to load

- You only need layout/theming.
- You only need state architecture (`state-management.md`).

## Core rules

- Validate locally for UX, but treat server validation as source of truth.
- Disable submit while loading.
- Show field errors near fields and global errors at the top.
- Keep controllers disposed.

## Minimal examples

Basic form pattern:

```dart
import 'package:flutter/material.dart';

class LoginForm extends StatefulWidget {
  const LoginForm({super.key, required this.onSubmit});
  final Future<void> Function({required String email, required String password}) onSubmit;

  @override
  State<LoginForm> createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  final _formKey = GlobalKey<FormState>();
  final _email = TextEditingController();
  final _password = TextEditingController();
  bool _loading = false;
  String? _error;

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    super.dispose();
  }

  Future<void> _submit() async {
    setState(() => _error = null);
    if (!(_formKey.currentState?.validate() ?? false)) return;

    setState(() => _loading = true);
    try {
      await widget.onSubmit(email: _email.text.trim(), password: _password.text);
    } catch (_) {
      setState(() => _error = 'Failed to sign in');
    } finally {
      if (mounted) setState(() => _loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          if (_error != null) Text(_error!, style: const TextStyle(color: Colors.red)),
          TextFormField(
            controller: _email,
            decoration: const InputDecoration(labelText: 'Email'),
            validator: (v) => (v ?? '').contains('@') ? null : 'Enter a valid email',
            keyboardType: TextInputType.emailAddress,
            textInputAction: TextInputAction.next,
          ),
          TextFormField(
            controller: _password,
            decoration: const InputDecoration(labelText: 'Password'),
            obscureText: true,
            validator: (v) => (v ?? '').length >= 8 ? null : 'Min 8 characters',
            onFieldSubmitted: (_) => _submit(),
          ),
          const SizedBox(height: 16),
          SizedBox(
            height: 48,
            child: FilledButton(
              onPressed: _loading ? null : _submit,
              child: _loading ? const CircularProgressIndicator() : const Text('Sign in'),
            ),
          ),
        ],
      ),
    );
  }
}
```

## Anti-patterns

- Submit button stays enabled during submission.
- Errors thrown straight to the UI with raw exception messages.
- Controllers not disposed.

## Checklist

- Field validation present.
- Loading disables submit.
- Errors are user-safe.
- Controllers disposed.

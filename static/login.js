function signInWithGoogle() {
    // Perform sign-in with Google functionality here
    console.log("Sign in with Google clicked");
    // Redirect to home page after successful sign-in
    window.location.href = "{{ url_for('static', filename='index.html') }}";
}

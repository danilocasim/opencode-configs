# Swift Configuration

## Swift Package Manager (Package.swift)

```swift
// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "MyProject",
    platforms: [.iOS(.v17), .macOS(.v14)],
    products: [
        .library(name: "MyProject", targets: ["MyProject"]),
    ],
    targets: [
        .target(name: "MyProject"),
        .testTarget(name: "MyProjectTests", dependencies: ["MyProject"]),
    ]
)
```

# Installation prerequisites (Windows)

You must perform the following steps before installing ROCm and check if the
system meets all the requirements to proceed with the installation.

## Confirm the system is supported

The ROCm installation is supported only on specific host architectures, Windows
Editions and update versions.

### Check the windows editions and update version on your system

This section discusses obtaining information about the host architecture,
Windows Edition and update version.

#### Command-line check

Verify the Windows Edition using the following steps:

1. To obtain the Linux distribution information, type the following command on
   your system from a PowerShell command-line interface (CLI):

   ```pwsh
   Get-ComputerInfo | Format-Table CsSystemType,OSName,OSDisplayVersion
   ```

2. Confirm that the obtained information matches with those listed in
   {ref}`windows-support`.

   **Example:** Running the command above on a Windows system may result in the
   following output:

   ```output
   CsSystemType OsName                   OSDisplayVersion
   ------------ ------                   ----------------
   x64-based PC Microsoft Windows 11 Pro 22H2
   ```

#### Graphical check

1. Open the Setting app.

   ![Gear icon of the Windows Settings app](../../../data/tutorials/install/windows/000-settings-dark.png "Windows Settings app icon")

   ![Gear icon of the Windows Settings app](../../../data/tutorials/install/windows/000-settings-light.png "Windows Settings app icon")

2. Navigate to **System > About**.

   ![Settings app panel showing device and OS information](../../../data/tutorials/install/windows/001-about-dark.png "Settings > About page")

   ![Settings app panel showing device and OS information](../../../data/tutorials/install/windows/001-about-light.png "Settings > About page")

3. Confirm that the obtained information matches with those listed in
   {ref}`windows-support`.

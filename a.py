import re

# Your regex pattern
pattern = r'(identifier="[A-Za-z]+" ID="[0-9]+")|(<[A-Za-z0-9]+ w="[0-9]+" i="[0-9]+" \/>)'

# Your input string
input_string = '''
<Item name="" identifier="dockinghatch" ID="719" rect="-400,457,128,112" NonInteractable="False" NonPlayerTeamInteractable="False" AllowSwapping="True" Rotation="0" Scale="0.5" SpriteColor="255,255,255,255" InventoryIconColor="255,255,255,255" ContainerColor="255,255,255,255" InvulnerableToDamage="False" Tags="dock" DisplaySideBySideWhenLinked="False" DisallowedUpgrades="" SpriteDepth="0.9" HiddenInGame="False" conditionpercentage="100">
    <DockingPort MainDockingPort="True" ApplyEffectsOnDocking="True" ForceDockingDirection="None" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <PowerTransfer CanBeOverloaded="False" OverloadVoltage="2" FireProbability="0" IsActive="True" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <Wire NoAutoLock="False" UseSpriteDepth="False" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <LightComponent Range="10" CastShadows="False" DrawBehindSubs="False" IsOn="False" Flicker="0" FlickerSpeed="1" PulseFrequency="0" PulseAmount="0" BlinkFrequency="0" LightColor="255,0,0,0" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="False" Msg="" />
    <LightComponent Range="10" CastShadows="False" DrawBehindSubs="False" IsOn="False" Flicker="0" FlickerSpeed="1" PulseFrequency="0" PulseAmount="0" BlinkFrequency="0" LightColor="0,255,0,0" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="False" Msg="" />
    <ConnectionPanel Locked="False" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="ItemMsgRewireScrewdriver">
      <requireditem items="screwdriver" type="Equipped" characterinventoryslottype="None" optional="false" ignoreineditor="false" excludebroken="true" requireempty="false" excludefullcondition="false" targetslot="-1" allowvariants="true" rotation="0" setactive="false" />
      <input name="toggle" />
      <input name="set_state">
        <link w="757" i="0" />
        <link w="758" i="0" />
      </input>
      <output name="power">
        <link w="503" i="1" />
      </output>
      <output name="state_out">
        <link w="759" i="0" />
        <link w="760" i="0" />
        <link w="761" i="0" />
      </output>
      <output name="proximity_sensor" />
    </ConnectionPanel>
  </Item>



<Item name="" identifier="dockinghatch" ID="719" rect="-400,457,128,112" NonInteractable="False" NonPlayerTeamInteractable="False" AllowSwapping="True" Rotation="0" Scale="0.5" SpriteColor="255,255,255,255" InventoryIconColor="255,255,255,255" ContainerColor="255,255,255,255" InvulnerableToDamage="False" Tags="dock" DisplaySideBySideWhenLinked="False" DisallowedUpgrades="" SpriteDepth="0.9" HiddenInGame="False" conditionpercentage="100">
    <DockingPort MainDockingPort="True" ApplyEffectsOnDocking="True" ForceDockingDirection="None" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <PowerTransfer CanBeOverloaded="False" OverloadVoltage="2" FireProbability="0" IsActive="True" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <Wire NoAutoLock="False" UseSpriteDepth="False" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <LightComponent Range="10" CastShadows="False" DrawBehindSubs="False" IsOn="False" Flicker="0" FlickerSpeed="1" PulseFrequency="0" PulseAmount="0" BlinkFrequency="0" LightColor="255,0,0,0" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="False" Msg="" />
    <LightComponent Range="10" CastShadows="False" DrawBehindSubs="False" IsOn="False" Flicker="0" FlickerSpeed="1" PulseFrequency="0" PulseAmount="0" BlinkFrequency="0" LightColor="0,255,0,0" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="False" Msg="" />
    <ConnectionPanel Locked="False" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="ItemMsgRewireScrewdriver">
      <requireditem items="screwdriver" type="Equipped" characterinventoryslottype="None" optional="false" ignoreineditor="false" excludebroken="true" requireempty="false" excludefullcondition="false" targetslot="-1" allowvariants="true" rotation="0" setactive="false" />
      <input name="toggle" />
      <input name="set_state">
        <link w="757" i="0" />
        <link w="758" i="0" />
      </input>
      <output name="power">
        <link w="503" i="1" />
      </output>
      <output name="state_out">
        <link w="759" i="0" />
        <link w="760" i="0" />
        <link w="761" i="0" />
      </output>
      <output name="proximity_sensor" />
    </ConnectionPanel>
  </Item>


  <Item name="" identifier="dockinghatch" ID="7139" rect="-400,457,128,112" NonInteractable="False" NonPlayerTeamInteractable="False" AllowSwapping="True" Rotation="0" Scale="0.5" SpriteColor="255,255,255,255" InventoryIconColor="255,255,255,255" ContainerColor="255,255,255,255" InvulnerableToDamage="False" Tags="dock" DisplaySideBySideWhenLinked="False" DisallowedUpgrades="" SpriteDepth="0.9" HiddenInGame="False" conditionpercentage="100">
    <DockingPort MainDockingPort="True" ApplyEffectsOnDocking="True" ForceDockingDirection="None" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <PowerTransfer CanBeOverloaded="False" OverloadVoltage="2" FireProbability="0" IsActive="True" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <Wire NoAutoLock="False" UseSpriteDepth="False" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="" />
    <LightComponent Range="10" CastShadows="False" DrawBehindSubs="False" IsOn="False" Flicker="0" FlickerSpeed="1" PulseFrequency="0" PulseAmount="0" BlinkFrequency="0" LightColor="255,0,0,0" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="False" Msg="" />
    <LightComponent Range="10" CastShadows="False" DrawBehindSubs="False" IsOn="False" Flicker="0" FlickerSpeed="1" PulseFrequency="0" PulseAmount="0" BlinkFrequency="0" LightColor="0,255,0,0" MinVoltage="0" PowerConsumption="0" Voltage="1" VulnerableToEMP="True" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="False" Msg="" />
    <ConnectionPanel Locked="False" PickingTime="0" CanBePicked="False" LockGuiFramePosition="False" GuiFrameOffset="0,0" AllowInGameEditing="True" Msg="ItemMsgRewireScrewdriver">
      <requireditem items="screwdriver" type="Equipped" characterinventoryslottype="None" optional="false" ignoreineditor="false" excludebroken="true" requireempty="false" excludefullcondition="false" targetslot="-1" allowvariants="true" rotation="0" setactive="false" />
      <input name="toggle" />
      <input name="set_state">
        <link w="757" i="0" />
        <link w="758" i="0" />
      </input>
      <output name="power">
        <link w="503" i="1" />
      </output>
      <output name="state_out">
        <link w="759" i="0" />
        <link w="760" i="0" />
        <link w="761" i="0" />
      </output>
      <output name="proximity_sensor" />
    </ConnectionPanel>
  </Item>






















'''

# Find all matches
matches = re.search(pattern, input_string)
print(re.search(pattern, input_string))